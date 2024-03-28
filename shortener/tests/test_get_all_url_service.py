import pytest

from source.application.get_all_url import GetAllUrlService
from source.adapters.repositories.url.fake import FakeUrlRepository

@pytest.mark.asyncio
async def test_new_url():
    fake_repo = FakeUrlRepository()
    service = GetAllUrlService(url_repo=fake_repo)
    
    urls = await service.execute(user_id=2)
    
    assert isinstance(urls,list)