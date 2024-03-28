from motor.motor_asyncio import AsyncIOMotorClient
from source.infraestructure.env import user, password,host

uri = f'mongodb://{user}:{password}@{host}'
url = 'mongodb://admin:123456@mongodb:27017'
conn = AsyncIOMotorClient(url)

default_db = conn.backend

urls_collection = default_db.urls