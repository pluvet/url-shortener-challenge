from hashlib import sha256
import jwt
from source.domain.user import User


def test_user_create():
    user = User("test@mail.com", "Password123")
    
    assert user.email == "test@mail.com"
    assert user.password == sha256("Password123".encode()).hexdigest()
    
def test_user_login_success():
    user = User("test@mail.com", "Password123")
    
    token = user.login("Password123")
    assert isinstance(token, jwt)
    
def test_user_login_fail():
    user = User("test@mail.com", "Password123")
    
    token = user.login("WrongPassword123")
    assert not isinstance(token, jwt)