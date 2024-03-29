from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: int | None = None
    email: EmailStr
    password: str
    
    def __init__(self, **data):
        super().__init__(**data)
        
    def login(self, password: str) -> bool:
        if self.password != password:
            return False
        return True

