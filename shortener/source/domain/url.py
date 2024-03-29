from pydantic import BaseModel

class Url(BaseModel):
    key: str 
    user_id: int
    long_url: str
    short_url: str
    visits: int = 0
    
    def new_visit (self):
        self.visits = self.visits + 1
