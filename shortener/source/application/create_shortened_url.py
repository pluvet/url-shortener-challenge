from dataclasses import dataclass
from source.ports.url_repository import UrlRepository
from source.domain.url import Url
from source.ports.key_generator import KeyGenerator
from source.application.exceptions import MaximumCollisionRetriesReached

@dataclass
class CreateShortenedUrlService():
    url_repo: UrlRepository
    key_generator: KeyGenerator

    async def execute(self, user_id, long_url: str, base_url: str) -> str:

        key=None
        retries = 3

        for retry in range(retries):
            key = self.key_generator.generate_key(length= 8+retry)
            key_exist = await self.url_repo.find(key=key)
            if key_exist is None:
                break

        if key is None:
            raise MaximumCollisionRetriesReached('maximum number of key collision retries reached!')

        url = Url(
            key=key,
            user_id=user_id, 
            long_url=long_url, 
            short_url=base_url+'/'+key
        )
        await self.url_repo.save(url)
        return url.short_url