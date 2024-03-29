from dataclasses import dataclass
import jwt
from source.infraestructure.env import secret

@dataclass
class TokenGenerator:

    def execute(self, user_id: int) -> str:
        return jwt.encode({"user_id": user_id}, secret, algorithm="HS256")
