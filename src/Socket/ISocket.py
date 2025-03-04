from abc import ABC, abstractmethod


class ISocket(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def send(self, emit_name: str, data: dict) -> bool:
        pass
