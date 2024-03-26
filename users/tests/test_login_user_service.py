import pytest
import jwt
from source.application.login_user import LoginUserService
from source.adapters.repositories.user.fake import FakeUserRepository


@pytest.mark.asyncio
async def test_login_user_service():
    fake_repo = FakeUserRepository()
    service = LoginUserService(fake_repo)
    token = service.execute()
    
    assert isinstance(token, jwt)