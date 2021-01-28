import asyncio
import time
from typing import Any, List, Mapping

from bson import ObjectId
from tartiflette import Resolver

from simtxt.db import db
from simtxt.index import index
from simtxt.tasks import new_task


async def get_texts(match=None):
    cursor = db.texts.aggregate(
        [
            {"$match": match or {}},
            {"$sort": {"created": -1}},
            {
                "$lookup": {
                    "from": "sentences",
                    "localField": "_id",
                    "foreignField": "textId",
                    "as": "sentences",
                }
            },
        ]
    )

    def process(text):
        text["id"] = str(text["_id"])
        text["sentences"] = [
            {**s, **{"id": str(s["_id"]), "textId": str(s["textId"])}}
            for s in text["sentences"]
        ]
        return text

    async for text in cursor:
        yield process(text)


# TODO: Handle similar
@Resolver("Query.text")
async def resolve_query_text(_, args: Mapping[str, Any], *__) -> Mapping[str, Any]:
    text = await get_texts({"_id": ObjectId(args["id"])}).__anext__()
    return text


@Resolver("Query.texts")
async def resolve_query_texts(*_) -> List:
    return [t async for t in get_texts()]


# TODO: Handle nested similar, don't query for similar if it's not included in fields
@Resolver("Query.sentence")
async def resolve_query_sentence(_, args: Mapping[str, Any], *__) -> Mapping[str, Any]:
    sentence = await db.sentences.find_one({"_id": ObjectId(args["id"])})
    sentence["id"] = args["id"]
    sentence["textId"] = str(sentence["textId"])
    await index.load()
    # this could block asyncio loop a little bit
    similar = index.query(sentence["content"])
    sentence["similar"] = [
        s for s in similar if s["sentence"]["textId"] != sentence["textId"]
    ]
    return sentence


@Resolver("Mutation.createText")
async def resolve_mutation_create_text(
    _, args: Mapping[str, Any], *__
) -> Mapping[str, Any]:
    text = {"content": args["content"]}
    result = await db.texts.insert_one({**text, **{"created": time.time()}})
    text["id"] = str(result.inserted_id)
    text["sentences"] = []
    asyncio.create_task(new_task("process_text", text["id"]))
    return text
