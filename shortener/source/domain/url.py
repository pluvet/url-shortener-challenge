from pydantic import BaseModel
import shortuuid

class Url(BaseModel):
    key: str | None = None
    user_id: int
    long_url: str
    short_url: str
    visits: int = 0
    
    def __init__(self, **data):
        super(Url, self).__init__(**data)
        if not self.key:
            self.key = self.__generate_short_url()
            self.short_url = self.short_url + '/' + self.key

    def __generate_short_url(self) -> str:
        return shortuuid.ShortUUID().random(length=6)
    
    def new_visit (self):
        self.visits = self.visits+1
