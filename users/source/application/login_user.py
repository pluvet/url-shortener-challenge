from dataclasses import dataclass
import jwt

from source.ports.user_repository import UserRepository
from source.application.exceptions import InvalidEmailOrPassword

@dataclass
class LoginUserService():
    user_repo: UserRepository

    async def execute(self, email: str, password: str) -> str:
        
        user = await self.user_repo.find_by_email(email)

        if user is None:
            raise InvalidEmailOrPassword(f'Incorrect Email')

        token = user.login(password=password)

        if token is None:
            raise InvalidEmailOrPassword(f'Incorret Password')

        return token