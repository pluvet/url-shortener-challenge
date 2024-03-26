import pytest

from source.domain.url import Url

@pytest.mark.asyncio
async def test_new_url():
    url = Url(user_id=1,long_url="www.test.com")
    
    assert url.key
    assert url.visits == 0

@pytest.mark.asyncio 
async def test_new_visit():
    url = Url(user_id=1,long_url="www.test.com")
    
    assert url.visits == 0
    
    url.new_visit()
    
    assert url.visits == 1