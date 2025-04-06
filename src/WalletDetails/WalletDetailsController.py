from .WalletDetailsService import WalletDetailsService
from src.__Parents.Controller import Controller
from .WalletDetailsRepository import WalletDetailsRepository
from src.Wallet.WalletMiddleware import WalletMiddleware
from ..Price.PriceRepository import PriceRepository
from ..Token.TokenRepository import TokenRepository


class WalletDetailsController(Controller):
    wallet_details_service = WalletDetailsService(wallet_details_repository=WalletDetailsRepository(), token_repository=TokenRepository(), price_repository=PriceRepository())

    @WalletMiddleware.check_authorize
    def post(self):
        res: dict = self.wallet_details_service.create(body=self.request.get_json())
        return res

    @WalletMiddleware.check_authorize
    def get(self):
        res: dict = self.wallet_details_service.get_details(network_id=int(self.arguments.get('network_id')))
        return res
