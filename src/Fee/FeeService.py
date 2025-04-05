import os
import requests

from src.Token.ITokenRepository import ITokenRepository
from src.__Parents.Rosponse import Response


class FeeService(Response):
    def __init__(self, token_repository: ITokenRepository):
        self.wrapper_url = os.environ.get('COIN_WRAPPER_URL')
        self.token_repository = token_repository

    def get_fee(self, network_id, symbol, from_address, to_address, amount):
        try:
            token = self.token_repository.get_by_network_id_token_symbol(network_id=network_id, token_symbol=symbol)
            response = requests.get(url=f"{self.wrapper_url}/fee?symbol={token.network.symbol}&contract_address={token.contract_address}&from_address={from_address}&to_address={to_address}&amount={amount}").json()
            if response['success']:
                return response['obj']
        except Exception as exc:
            return "0.0"
