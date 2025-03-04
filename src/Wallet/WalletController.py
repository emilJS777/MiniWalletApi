from .WalletService import WalletService
from src.__Parents.Controller import Controller
from .WalletRepository import WalletRepository


class WalletController(Controller):
    wallet_service = WalletService(wallet_repository=WalletRepository())

    def post(self):
        res: dict = self.wallet_service.create(body=self.request.get_json())
        return res

    def get(self):
        if(self.arguments.get('hash')):
            res: dict = self.wallet_service.get(self.arguments.get('hash'))
        return res
