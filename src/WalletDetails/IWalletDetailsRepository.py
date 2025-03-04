from abc import ABC, abstractmethod
from .WalletDetailsModel import WalletDetails

class IWalletDetailsRepository(ABC):
    @abstractmethod
    def create(self, body: dict, wallet_id: int, qr: str) -> WalletDetails:
        pass

    @abstractmethod
    def get(self, wallet_id: int, network_id: int) -> WalletDetails:
        pass
