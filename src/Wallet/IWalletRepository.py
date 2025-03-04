from abc import ABC, abstractmethod
from .WalletModel import Wallet

class IWalletRepository(ABC):
    @abstractmethod
    def create(self, body: dict) -> Wallet:
        pass

    @abstractmethod
    def get_by_id(self, wallet_id) -> Wallet:
        pass

    @abstractmethod
    def get_all(self) -> list[Wallet]:
        pass

    @abstractmethod
    def get_by_hash(self, wallet_hash) -> Wallet:
        pass