from dataclasses import dataclass

from source.domain.url import Url
from source.ports.url_repository import UrlRepository


@dataclass
class GetAllUrlService():
    url_repo: UrlRepository

    async def execute(self, user_id: int) -> list[Url]:
        return await self.url_repo.list_by_user_id(user_id=user_id)