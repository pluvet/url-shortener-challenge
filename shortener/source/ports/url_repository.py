from abc import ABC, abstractmethod

from source.domain.url import Url


class UrlRepository(ABC):
    @abstractmethod
    async def save(self, url: Url) -> str:
        raise NotImplementedError
    @abstractmethod
    async def find(self, key: str) -> Url:
        raise NotImplementedError