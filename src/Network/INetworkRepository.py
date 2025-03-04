from abc import ABC, abstractmethod
from .NetworkModel import Network

class INetworkRepository(ABC):
    @abstractmethod
    def create(self, body: dict):
        pass

    @abstractmethod
    def update(self, network: Network, body: dict):
        pass

    @abstractmethod
    def delete(self, network: Network):
        pass

    @abstractmethod
    def get_by_id(self, network_id) -> Network:
        pass

    @abstractmethod
    def get_all(self) -> list[Network]:
        pass