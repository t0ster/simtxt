import asyncio

import spacy
from bson import ObjectId

from aiotasks import build_manager
from simtxt.db import db
from simtxt.index import Index

NLP = spacy.load("en_core_web_sm")

manager = build_manager(dsn="redis://")


@manager.task()
async def process_text(id_):
    text_id = ObjectId(id_)
    text = await db.texts.find_one({"_id": text_id})
    await db.sentences.insert_many(
        [{"textId": text_id, "content": str(s)} for s in NLP(text["content"]).sents]
    )
    index = await Index.create()
    await index.dump()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(process_text("600f530222136b00409b1940"))
