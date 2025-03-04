from src.Wallet.WalletRepository import WalletRepository
from src.__Parents.Rosponse import Response

class WalletService(Response):
    def __init__(self, wallet_repository: WalletRepository):
        self.wallet_repository = wallet_repository

    def create(self, body: dict) -> dict:
        wallet = self.wallet_repository.get_by_hash(wallet_hash=body['hash'])
        if not wallet:
            wallet = self.wallet_repository.create(body=body)

        return self.response_ok({
            'id': wallet.id,
            'hash': wallet.hash
        })

    def get_by_hash(self, wallet_hash: str) -> dict:
        wallet = self.wallet_repository.get_by_hash(wallet_hash)
        if not wallet:
            return self.response_not_found()

        return self.response_ok({
            'id': wallet.id,
            'hash': wallet.hash
        })
