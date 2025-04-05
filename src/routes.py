from src import api

from src.Network.NetworkController import NetworkController
api.add_resource(NetworkController, "/network")

from src.Token.TokenController import TokenController
api.add_resource(TokenController, "/token")

from src.Wallet.WalletController import WalletController
api.add_resource(WalletController, "/wallet")

from src.WalletDetails.WalletDetailsController import WalletDetailsController
api.add_resource(WalletDetailsController, "/walletDetails")

from src.Transaction.TransactionController import TransactionController
api.add_resource(TransactionController, "/transaction")

from src.Fee.FeeController import FeeController
api.add_resource(FeeController, "/fee")
