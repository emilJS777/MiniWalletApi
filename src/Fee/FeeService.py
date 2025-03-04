import os
import requests
from src.__Parents.Rosponse import Response


class FeeService(Response):
    def __init__(self):
        self.wrapper_url = os.environ.get('COIN_WRAPPER_URL')

    def get_fee(self, network_symbol: str, gas_limit: int):
        response = requests.get(url=f"{self.wrapper_url}/fee?symbol={network_symbol}&gas_limit={gas_limit}").json()
        if response['success']:
            return response['obj']
        return "0"