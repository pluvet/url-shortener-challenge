from pydantic import BaseModel, EmailStr
import jwt
from hashlib import sha256
from source.infraestructure.jwt.config import secret

class User(BaseModel):
    id: int | None = None
    email: EmailStr
    password: str
    
    def __init__(self, email: EmailStr, password: str):
        self.email = email
        self.password = sha256(password.encode()).hexdigest()
        
    def login(self, password: str) -> jwt:
        if self.password != sha256(password.encode()).hexdigest():
            return False
        return jwt.encode({"user_id": self.id}, secret, algorithm="HS256")
