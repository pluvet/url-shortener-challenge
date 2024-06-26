import pytest

from source.application.redirect_url import RedirectUrlService
from source.adapters.repositories.url.fake import FakeUrlRepository

@pytest.mark.asyncio
async def test_new_url():
    fake_repo = FakeUrlRepository()
    service = RedirectUrlService(url_repo=fake_repo)
    
    long_url = await service.execute(key="TEST1")
    
    assert isinstance(long_url,str)