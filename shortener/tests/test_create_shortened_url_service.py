import pytest

from source.application.create_shortened_url import CreateShortenedUrlService
from source.adapters.repositories.url.fake import FakeUrlRepository

@pytest.mark.asyncio
async def test_new_url():
    fake_repo = FakeUrlRepository()
    service = CreateShortenedUrlService(url_repo=fake_repo)
    
    url_key = service.execute(user_id=1, long_url="www.long_url.com")
    
    assert url_key
