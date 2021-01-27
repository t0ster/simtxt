import pickle
from collections import defaultdict
from typing import Any, List, Optional

from gensim import corpora, models, similarities
from gridfs.errors import NoFile
from motor.motor_asyncio import AsyncIOMotorGridFSBucket

from simtxt.db import db
from simtxt.misc import stoplist


class Index:
    index: Optional[Any]
    dictionary: Optional[Any]
    corpus: Optional[Any]
    model: Optional[Any]
    documents: Optional[Any]
    md5: Optional[str]
    _id: Optional[str]

    @classmethod
    async def create(cls) -> "Index":
        self = Index()
        await self.reindex()
        return self

    def query(self, text, min_score=0.1) -> List:
        vec_bow = self.dictionary.doc2bow(text.lower().split())
        vec_lsi = self.model[vec_bow]  # convert the query to LSI space
        sims = self.index[vec_lsi]
        sims = sorted(enumerate(sims), key=lambda item: -item[1])
        return [
            {
                "score": doc_score,
                "sentence": {
                    "id": str(self.documents[doc_position]["obj"]["_id"]),
                    "textId": str(self.documents[doc_position]["obj"]["textId"]),
                    "content": self.documents[doc_position]["obj"]["content"],
                },
            }
            for doc_position, doc_score in sims
            if doc_score > min_score
        ]

    async def reindex(self) -> None:
        cursor = db.sentences.find()
        # stoplist = set("for a of the and to in".split())

        async def process_texts():
            frequency = defaultdict(int)
            async for mongo_document in cursor:
                raw_text = mongo_document["content"]
                text = [
                    word for word in raw_text.lower().split() if word not in stoplist
                ]
                for token in text:
                    frequency[token] += 1
                yield {
                    # to remove words that appear only once change 0 to 1
                    "tokenized": [token for token in text if frequency[token] > 0],
                    "obj": mongo_document,
                }

        texts = [t async for t in process_texts()]

        dictionary = corpora.Dictionary((text["tokenized"] for text in texts))
        corpus = [dictionary.doc2bow(text["tokenized"]) for text in texts]

        lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=100)
        index = similarities.MatrixSimilarity(lsi[corpus])
        self.index = index
        self.dictionary = dictionary
        self.corpus = corpus
        self.model = lsi
        self.documents = texts

    async def dump(self) -> None:
        """Pickles index and loads data to MongoDB"""
        data = pickle.dumps(
            (self.index, self.dictionary, self.corpus, self.model, self.documents)
        )
        fs = AsyncIOMotorGridFSBucket(db)
        try:
            grid_out = await fs.open_download_stream_by_name("index")
            fs.delete(grid_out._id)
        except NoFile:
            pass
        grid_in = fs.open_upload_stream("index")
        await grid_in.write(data)
        await grid_in.close()
        self.md5 = grid_in.md5
        self._id = str(grid_in._id)

    async def load(self, force=False) -> None:
        """Loads index from MongoDB

        It is safe to call `index.load()` in each request handler because
        whole data is fetched only if local and remote md5 hash doesn't match
        """
        fs = AsyncIOMotorGridFSBucket(db)
        grid_out = await fs.open_download_stream_by_name("index")
        if force or grid_out.md5 != self.md5:
            data = pickle.loads(await grid_out.read())
            self.index, self.dictionary, self.corpus, self.model, self.documents = data
            self.md5 = grid_out.md5
            self._id = grid_out._id
