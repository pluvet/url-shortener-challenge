from dataclasses import dataclass

from source.ports.url_repository import UrlRepository


@dataclass
class RedirectUrlService():
    url_repo: UrlRepository

    async def execute(self, key: str) -> str:
        url = await self.url_repo.find(key)
        url.new_visit()
        await self.url_repo.save(url)
        return url.long_url
