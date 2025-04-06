from abc import ABC, abstractmethod
from .PriceModel import Price

class IPriceRepository(ABC):
    @abstractmethod
    def create(self, body):
        pass

    @abstractmethod
    def get_all(self) -> list[Price]:
        pass