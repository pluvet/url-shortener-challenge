from dataclasses import dataclass
from source.domain.user import User

@dataclass
class FakeUserRepository:

    async def save(self, user: User) -> str:
        return 1
    
    async def find_by_email(self, email: str) -> User:
        user = User(email, "fake123")
        return user