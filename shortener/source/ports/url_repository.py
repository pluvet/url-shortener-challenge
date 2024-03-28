from abc import ABC, abstractmethod
from source.domain.url import Url


class UrlRepository(ABC):
    @abstractmethod
    async def save(self, url: Url) -> None:
        raise NotImplementedError
    @abstractmethod
    async def find(self, key: str) -> Url:
        raise NotImplementedError
    @abstractmethod
    async def list_by_user_id(self, user_id: str) -> list[Url]:
        raise NotImplementedError
    @abstractmethod
    async def update(self, url: Url) -> None:
        raise NotImplementedError