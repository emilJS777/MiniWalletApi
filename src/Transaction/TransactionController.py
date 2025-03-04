from src.__Parents.Controller import Controller
from .TransactionService import TransactionService
from src.Token.TokenRepository import TokenRepository


class TransactionController(Controller):
    transaction_service = TransactionService(token_repository=TokenRepository())

    def get(self):
        res: dict = self.transaction_service.get_transactions(network_id=int(self.request.args.get('network_id')),
                                                              symbol=self.request.args.get('symbol'),
                                                              address=self.request.args.get('address'),
                                                              limit=int(self.request.args.get('limit')),
                                                              offset=int(self.request.args.get('offset')))
        return res

    def post(self):
        res: dict = self.transaction_service.create_unsigned_transaction(body=self.request.get_json())
        return res

    def patch(self):
        res: dict = self.transaction_service.send_signed_transaction(body=self.request.get_json())
        return res