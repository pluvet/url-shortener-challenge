from pydantic import BaseModel
import random
import string

class Url(BaseModel):
    id: int | None = None
    key: str
    long_url: str
    short_url: str
    
    def __init__(self, long_url: str, self_url: str):
        self.long_url = long_url
        self.key = self.__generate_short_url()
        self.short_url = self_url + self.key

    def __generate_short_url(self, length=6) -> str:
        chars = string.ascii_letters + string.digits
        return "".join(random.choice(chars) for _ in range(length))
