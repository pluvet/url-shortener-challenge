from source.domain.url import Url
from source.ports.url_repository import UrlRepository

class FakeUrlRepository(UrlRepository):

    async def save(self, url: Url) -> str:
        return 1
    
    async def find(self, key: str) -> Url:
        url = Url(user_id=2, long_url="www.fake.com")
        return url