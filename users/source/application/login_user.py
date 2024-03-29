from dataclasses import dataclass
import jwt

from source.ports.user_repository import UserRepository
from source.ports.password_encrypter import HashPasswordEncrypter
from source.ports.token_generator import TokenGenerator
from source.application.exceptions import InvalidEmailOrPassword

@dataclass
class LoginUserService():
    user_repo: UserRepository
    password_encrypter: HashPasswordEncrypter
    token_generator: TokenGenerator

    async def execute(self, email: str, password: str) -> str:
        
        user = await self.user_repo.find_by_email(email)

        if user is None:
            raise InvalidEmailOrPassword(f'Incorrect Email')
        
        encrypted_password = self.password_encrypter.execute(password)

        login = user.login(password=encrypted_password)

        if not login:
            raise InvalidEmailOrPassword(f'Incorret Password')

        return self.token_generator.execute(user.id)