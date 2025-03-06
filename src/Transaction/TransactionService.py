import os
import requests

from src.Network.INetworkRepository import INetworkRepository
from src.Token.ITokenRepository import ITokenRepository
from src.__Parents.Rosponse import Response


class TransactionService(Response):
    def __init__(self, token_repository: ITokenRepository, network_repository: INetworkRepository):
        self.wrapper_url = os.environ.get('COIN_WRAPPER_URL')
        self.token_repository = token_repository
        self.network_repository = network_repository

    def get_transactions(self, network_id: int, address: str, limit: int, offset: int):
        try:
            network = self.network_repository.get_by_id(network_id=network_id)

            history_list = []
            response = requests.get(url=f"{self.wrapper_url}/transaction?symbol={network.symbol}&address={address}&limit={limit}&offset={offset}")


            if response.status_code == 200:
                history_list = history_list + response.json().get('obj')
            print(history_list)
            return self.response_ok(history_list)
        except Exception as e:
            print(f"get transactions failed {e}")
            return self.response_err_msg(f'get transactions failed {e}')

    def create_unsigned_transaction(self, body: dict) -> dict:
        try:
            token = self.token_repository.get_by_network_id_token_symbol(network_id=body['network_id'],
                                                                         token_symbol=body['symbol'])
            if not token:
                return self.response_not_found()
            response = requests.post(url=f"{self.wrapper_url}/transaction", json={'symbol': token.network.symbol,
                                                                 'from_address': body['from_address'],
                                                                 'to_address': body['to_address'],
                                                                 'amount': body['amount'],
                                                                 'contract_address': token.contract_address})

            if response.status_code == 200:
                return self.response_ok(response.json().get('obj'))
            else:
                return self.response_err_msg(response.json().get('obj').get('msg'))
        except Exception as e:
            print(f"create unsigned transaction failed {e}")
            return self.response_err_msg(f'create unsigned transaction failed {e}')

    def send_signed_transaction(self, body: dict) -> dict:
        try:
            token = self.token_repository.get_by_network_id_token_symbol(network_id=body['network_id'],
                                                                         token_symbol=body['symbol'])
            if not token:
                return self.response_not_found()

            response = requests.patch(url=f"{self.wrapper_url}/transaction", json={'symbol': token.network.symbol, 'signed_txn': body['signed_txn']})
            if response.status_code == 200:
                print(response.json().get('obj'))
                return self.response_ok(response.json())
            else:
                return self.response_err_msg(response.json().get('obj').get('msg'))

        except Exception as e:
            print(f"Send signed transaction failed {e}")
            return self.response_err_msg(f'Send signed transaction failed {e}')
        # {
        #     "symbol": "TRX",
        #     "signed_txn": ""s
        # }
        pass
