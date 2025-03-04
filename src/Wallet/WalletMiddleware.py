from functools import wraps
from flask import g, request
from src.Wallet.IWalletRepository import IWalletRepository
from src.Wallet.WalletRepository import WalletRepository
from src.__Parents.Rosponse import Response


class WalletMiddleware(Response):
    wallet_repository: IWalletRepository = WalletRepository()

    @staticmethod
    def check_authorize(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            hash = request.headers.get('AuthorizationWallet')
            if not hash:
                return WalletMiddleware.response_invalid_wallet("You don't have a wallet")
            wallet = WalletMiddleware.wallet_repository.get_by_hash(wallet_hash=hash)
            if not wallet:
                return WalletMiddleware.response_invalid_wallet("You don't have a wallet")
            g.wallet = wallet
            return f(*args, **kwargs)
        return decorated_function

