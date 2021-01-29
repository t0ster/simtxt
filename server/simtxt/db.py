import motor.motor_asyncio

from simtxt.config import settings


class Db(motor.motor_asyncio.AsyncIOMotorDatabase):
    texts: motor.motor_asyncio.AsyncIOMotorCollection
    sentences: motor.motor_asyncio.AsyncIOMotorCollection
    queue: motor.motor_asyncio.AsyncIOMotorCollection


class Client(motor.motor_asyncio.AsyncIOMotorClient):
    simtxt: Db


class DB:
    db: Db

    async def init_db(self):
        client: Client = Client(settings.db_uri)
        self.db = client.simtxt
        if "queue" not in await self.db.list_collection_names():
            await self.db.create_collection(
                "queue", capped=True, size=128 * 1024 * 1024
            )
        await self.db.sentences.create_index("textId")

    def __call__(self) -> Db:
        return self.db


db = DB()
