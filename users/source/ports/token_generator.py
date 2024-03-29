from abc import ABC, abstractmethod

class TokenGenerator (ABC):

    @abstractmethod
    def execute(self, user_id: int) -> str:
        raise NotImplementedError
    
