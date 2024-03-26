import pytest
from source.application.register_user import RegisterUserService
from source.adapters.repositories.user.fake import FakeUserRepository


@pytest.mark.asyncio
async def test_register_user_service():
    fake_repo = FakeUserRepository()
    service = RegisterUserService(fake_repo)
    user_id = service.execute()
    
    assert isinstance(user_id, int)