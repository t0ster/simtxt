import motor.motor_asyncio


class Db(motor.motor_asyncio.AsyncIOMotorDatabase):
    texts: motor.motor_asyncio.AsyncIOMotorCollection
    sentences: motor.motor_asyncio.AsyncIOMotorCollection
    queue: motor.motor_asyncio.AsyncIOMotorCollection


class Client(motor.motor_asyncio.AsyncIOMotorClient):
    simtxt: Db


client: Client = Client()
db = client.simtxt


async def init_db():
    if "queue" not in await db.list_collection_names():
        await db.create_collection("queue", capped=True, size=128 * 1024 * 1024)
