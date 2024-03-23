from abc import ABC, abstractmethod

from source.domain.user import User


class UserRepository(ABC):
    @abstractmethod
    async def save(self, user: User) -> str:
        raise NotImplementedError
    @abstractmethod
    async def find_by_email(self, email: str) -> User:
        raise NotImplementedError