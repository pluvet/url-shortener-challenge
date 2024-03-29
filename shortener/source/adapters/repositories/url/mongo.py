
from dataclasses import dataclass
from motor.motor_asyncio import AsyncIOMotorCollection

from source.infraestructure.mongo import urls_collection
from source.domain.url import Url
from source.infraestructure.mongo import conn
from source.ports.url_repository import UrlRepository

@dataclass
class UrlMongoRepository(UrlRepository):
    """url class"""
    collection: AsyncIOMotorCollection = urls_collection

    async def list_by_user_id(self, user_id: int) -> list[Url]:
        """get all url"""

        urls = await self.collection.find({'user_id':user_id}).to_list(length=None)
        return [
            Url(
                key = url["_id"],
                user_id = url["user_id"],
                long_url = url["long_url"],
                short_url = url["short_url"],
                visits = url["visits"]
            )
            for url in urls
        ]
    
    async def save(self, url: Url) -> None:
        """update or create a single url"""

        await self.collection.insert_one(
            {
                'user_id':url.user_id,
                'long_url':url.long_url,
                'visits':url.visits,
                'short_url': url.short_url,
                '_id':url.key
            }
        )

    async def update(self, url: Url) -> None:
        """update or create a single url"""

        await self.collection.update_one(
            {"_id":url.key},
            {"$set": {
                "user_id":url.user_id,
                "long_url":url.long_url,
                "visits":url.visits,
                "short_url": url.short_url,
                "_id":url.key
            }}
        )
        
    async def find(self, key: str) -> Url | None:

        url = await self.collection.find_one({"_id":key})
        
        if url is None:
            return None

        return Url(
            key = url["_id"],
            user_id = url["user_id"],
            long_url = url["long_url"],
            short_url = url["short_url"],
            visits = url["visits"]
        )
