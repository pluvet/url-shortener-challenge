from dataclasses import dataclass

from source.ports.url_repository import UrlRepository
from source.application import exceptions


@dataclass
class RedirectUrlService():
    url_repo: UrlRepository

    async def execute(self, key: str) -> str:
        url = await self.url_repo.find(key)
        if url is None:
            raise exceptions.NotFound(f'Url with key {key} not found')

        url.new_visit()
        await self.url_repo.update(url)
        return url.long_url
