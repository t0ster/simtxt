import logging
import time

import spacy
from bson import ObjectId

from simtxt.db import db
from simtxt.index import Index

logger = logging.getLogger("simtxt.tasks")


NLP = spacy.load("en_core_web_sm")


async def process_text(id_):
    logger.info("Processing text %s and refreshing index", id_)
    text_id = ObjectId(id_)
    text = await db.texts.find_one({"_id": text_id})
    await db.sentences.insert_many(
        [{"textId": text_id, "content": str(s)} for s in NLP(text["content"]).sents]
    )
    index = await Index.create()
    await index.dump()


async def new_task(task: str, *args) -> None:
    await db.queue.insert_one(
        {
            "task": task,
            "args": args,
            "ts": time.time(),
        }
    )
