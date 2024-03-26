
from dataclasses import dataclass

from source.domain.url import Url
from source.infraestructure.mongo import conn
from source.ports.url_repository import UrlRepository

@dataclass
class UrlMongoRepository(UrlRepository):
    """url class"""
    
    async def save(self, url: Url) -> None:
        """update or create a single url"""

        await conn.local.url.insert_one(
            {
                'user_id':url.user_id,
                'long_url':url.long_url,
                'visits':url.visits,
                '_id':url.key
            }
        )
        
    async def find(self, key: str) -> Url:

        url = await conn.local.url.find_one({'_id':key})
        
        if url is None:
            return None

        return Url(
            key = url["_id"],
            user_id = url["user_id"],
            long_url = url["long_url"],
            visits = url["visits"]
        )
        