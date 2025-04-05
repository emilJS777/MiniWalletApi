import time

from .IUpdaterService import IUpdaterService
# from ..Fee.FeeService import FeeService
from ..Price.PriceService import PriceService
from ..Socket.ISocket import ISocket
from ..Token.TokenRepository import TokenRepository


class UpdaterService(IUpdaterService):
    def __init__(self, socket: ISocket, token_repository: TokenRepository):
        self.socket = socket
        self.price_service = PriceService()
        # self.fee_service = FeeService()
        self.token_repository = token_repository
    #
    # def start_fee_updated(self):
    #     tokens = self.token_repository.get_all()
    #     while True:
    #         fee_data = []
    #         for token in tokens:
    #             fee = self.fee_service.get_fee(network_symbol=token.network.symbol, gas_limit=token.gas_limit)
    #             fee_data.append({"symbol": token.symbol, "network_symbol": token.network.symbol, "fee": fee})
    #         self.socket.send("onFee", {"feeData": fee_data})
    #         time.sleep(2)

    def start_price_updated(self):
        tokens = self.token_repository.get_all()
        while True:
            price_table = self.price_service.get_price_table()
            price_data = []
            for token in tokens:
                usd_price, change_24h = self.price_service.get_price(external_price_table=price_table, label=token.price_key)
                price_data.append({"symbol": token.symbol, "usd_price": usd_price, "change_24h": change_24h})
            self.socket.send("onPrice", {"priceData": price_data})
            time.sleep(20)

