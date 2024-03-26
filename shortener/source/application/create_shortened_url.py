from dataclasses import dataclass
from source.ports.url_repository import UrlRepository
from source.domain.url import Url
from source.infraestructure.env import short_url

@dataclass
class CreateShortenedUrlService():
    url_repo: UrlRepository

    async def execute(self, user_id, long_url: str) -> Url:
        
        url = Url(
            user_id=user_id, 
            long_url=long_url, 
            short_url=short_url
        )
        await self.url_repo.save(url)
        return url