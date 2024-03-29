from dataclasses import dataclass
from hashlib import sha256
        
@dataclass
class HashPasswordEncrypter:

    def execute(self, password: str) -> str:
        return sha256(password.encode()).hexdigest()
        