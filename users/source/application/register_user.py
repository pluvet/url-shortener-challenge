from dataclasses import dataclass

from source.ports.user_repository import UserRepository
from source.ports.password_encrypter import HashPasswordEncrypter
from source.domain.user import User


@dataclass
class RegisterUserService():
    user_repo: UserRepository
    password_encrypter: HashPasswordEncrypter

    async def execute(self, email: str, password: str) -> int:
        
        new_user = User(
            email=email,
            password=self.password_encrypter.execute(password)
        )
        return await self.user_repo.save(user=new_user)
