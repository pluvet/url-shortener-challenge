from motor.motor_asyncio import AsyncIOMotorClient
from source.infraestructure.env import user, password,host

uri = f'mongodb://{user}:{password}@{host}'

conn = AsyncIOMotorClient(uri, port=27017)