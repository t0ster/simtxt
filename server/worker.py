import asyncio
import logging

from pymongo.cursor import CursorType

from simtxt import tasks
from simtxt.db import db, init_db
from simtxt.logging import init_logging

init_logging(logging.DEBUG)
logger = logging.getLogger("simtxt.worker")


# XXX: Currently only one instnce of running worker is supported
async def main():
    await init_db()
    try:
        first = await db.queue.find().sort("$natural", -1).limit(-1).next()
        ts = first["ts"]
        logger.debug("First: %s", first)
    except StopAsyncIteration:
        ts = 0
    while True:
        cursor = db.queue.find(
            {"ts": {"$gt": ts}}, cursor_type=CursorType.TAILABLE_AWAIT
        )
        while cursor.alive:
            async for task in cursor:
                ts = task["ts"]
                logger.info("Got new task: %s", task)
                if task["task"] == "process_text":
                    text_id = task["args"][0]
                    # this is blocking asyncio loop
                    # however we should not care because this is worker
                    await tasks.process_text(text_id)
            await asyncio.sleep(1)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
