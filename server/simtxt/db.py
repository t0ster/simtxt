import motor.motor_asyncio


class Db(motor.motor_asyncio.AsyncIOMotorDatabase):
    texts: motor.motor_asyncio.AsyncIOMotorCollection
    sentences: motor.motor_asyncio.AsyncIOMotorCollection


class Client(motor.motor_asyncio.AsyncIOMotorClient):
    simtxt: Db


client: Client = motor.motor_asyncio.AsyncIOMotorClient()
db = client.simtxt
