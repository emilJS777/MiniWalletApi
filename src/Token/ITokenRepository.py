from abc import ABC, abstractmethod
from .TokenModel import Token

class ITokenRepository(ABC):
    @abstractmethod
    def create(self, body: dict):
        pass

    @abstractmethod
    def update(self, token: Token, body: dict):
        pass

    @abstractmethod
    def delete(self, token: Token):
        pass

    @abstractmethod
    def get_by_id(self, token_id) -> Token:
        pass

    @abstractmethod
    def get_by_network_id_token_symbol(self, network_id: int, token_symbol) -> Token:
        pass

    @abstractmethod
    def get_all(self) -> list[Token]:
        pass

    @abstractmethod
    def get_all_by_network_id(self, network_id: int) -> list[Token]:
        pass