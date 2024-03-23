from dataclasses import dataclass
from source.ports.user_repository import UserRepository
import jwt

@dataclass
class LoginUserService():
    user_repo: UserRepository

    async def execute(self, email: str, password: str) -> jwt:
        
        user = await self.user_repo.find_by_email(email)
        token = user.login(password=password)
        return token