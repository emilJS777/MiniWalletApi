from abc import ABC, abstractmethod

class IUpdaterService(ABC):
    # @abstractmethod
    # def start_fee_updated(self):
    #     pass

    @abstractmethod
    def start_price_updated(self):
        pass