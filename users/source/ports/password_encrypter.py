from abc import ABC, abstractmethod
        
class HashPasswordEncrypter (ABC):

    @abstractmethod
    def execute(self, password: str) -> str:
        raise NotImplementedError