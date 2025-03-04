from .IWalletRepository import IWalletRepository
from src.Wallet.WalletModel import Wallet

class WalletRepository(IWalletRepository):

    def create(self, body: dict) -> Wallet:
        wallet = Wallet()
        wallet.hash = body['hash']
        wallet.save_db()
        return wallet

    def get_by_id(self, wallet_id) -> Wallet:
        wallet = Wallet.query.filter_by(id=wallet_id).first()
        return wallet

    def get_all(self) -> list[Wallet]:
        wallets = Wallet.query.all()
        return wallets

    def get_by_hash(self, wallet_hash) -> Wallet:
        wallet = Wallet.query.filter_by(hash=wallet_hash).first()
        return wallet