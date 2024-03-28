from motor.motor_asyncio import AsyncIOMotorClient

from source.infraestructure.env import mongo_url

conn = AsyncIOMotorClient(mongo_url)

default_db = conn.backend

urls_collection = default_db.urls