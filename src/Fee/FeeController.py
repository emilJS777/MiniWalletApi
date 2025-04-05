from src.Token.TokenRepository import TokenRepository
from src.__Parents.Controller import Controller
from src.Fee.FeeService import FeeService

class FeeController(Controller):
    fee_service = FeeService(TokenRepository())

    def get(self):
        res: dict = self.fee_service.get_fee(network_id=int(self.arguments.get('network_id')),
                                             from_address=self.arguments.get('from_address'),
                                             to_address=self.arguments.get('to_address'),
                                             amount=self.arguments.get('amount'),
                                             symbol=self.arguments.get('symbol'))
        return res