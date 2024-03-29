from abc import ABC, abstractmethod

class KeyGenerator(ABC):

    @abstractmethod
    def generate_key(self, length=8) -> str:
        raise NotImplementedError