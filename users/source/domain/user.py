from pydantic import BaseModel, EmailStr
import jwt
from hashlib import sha256
from source.infraestructure.jwt import secret

class User(BaseModel):
    id: int | None = None
    email: EmailStr
    password: str
    
    def __init__(self, **data):
        super().__init__(**data)
        if not self.id:
            self.password = sha256(self.password.encode()).hexdigest()
        
    def login(self, password: str) -> str | None:
        if self.password != sha256(password.encode()).hexdigest():
            return None
        return jwt.encode({"user_id": self.id}, secret, algorithm="HS256")
