from operator import index

from sqlalchemy.util import symbol

from .ITokenRepository import ITokenRepository
from src.Token.TokenModel import Token

class TokenRepository(ITokenRepository):

    def create(self, body: dict):
        token = Token()
        token.symbol = body['symbol']
        token.label = body['label']
        token.network_id = body['network_id']
        token.contract_address = body['contract_address']
        token.native = body['native']
        token.index = body['index']
        token.price_key = body['price_key']
        token.gas_limit = body['gas_limit']
        token.save_db()

    def update(self, token: Token, body: dict):
        token.symbol = body['symbol']
        token.label = body['label']
        token.network_id = body['network_id']
        token.contract_address = body['contract_address']
        token.native = body['native']
        token.index = body['index']
        token.price_key = body['price_key']
        token.gas_limit = body['gas_limit']
        token.update_db()

    def delete(self, token: Token):
        token.delete_db()

    def get_by_id(self, token_id) -> Token:
        token = Token.query.filter_by(id=token_id).first()
        return token

    def get_by_network_id_token_symbol(self, network_id: int, token_symbol) -> Token:
        token = Token.query.filter_by(network_id=network_id, symbol=token_symbol).first()
        return token

    def get_all(self) -> list[Token]:
        token = Token.query.order_by(Token.index).all()
        return token

    def get_all_by_network_id(self, network_id: int) -> list[Token]:
        tokens = Token.query.filter_by(network_id=network_id).order_by(Token.index).all()
        return tokens