from dataclasses import dataclass

from source.ports.user_repository import UserRepository
from source.domain.user import User


@dataclass
class RegisterUserService():
    user_repo: UserRepository

    async def execute(self, email: str, password: str) -> int:
        
        new_user = User(
            email=email,
            password=password
        )
        return await self.user_repo.save(user=new_user)
