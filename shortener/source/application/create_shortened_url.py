from dataclasses import dataclass
from source.ports.user_repository import UserRepository
from source.domain.url import Url

@dataclass
class LoginUserService():
    url_repo: UserRepository

    async def execute(self, long_url: str) -> Url:
        
        url = Url(long_url=long_url, self_url="https:localhost.com")
        await self.url_repo.save(url)
        return url