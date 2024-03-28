from source.domain.url import Url
from source.ports.url_repository import UrlRepository

class FakeUrlRepository(UrlRepository):

    async def list_by_user_id(self, user_id: str) -> list[Url]:
        return []

    async def save(self, url: Url) -> None:
        return None
    
    async def find(self, key: str) -> Url:
        url = Url(user_id=2, long_url="www.fake.com", short_url="localhost")
        return url
    
    async def update(self, url: Url) -> None:
        return None
    