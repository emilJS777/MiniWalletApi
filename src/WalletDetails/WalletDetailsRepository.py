from .IWalletDetailsRepository import IWalletDetailsRepository
from src.WalletDetails.WalletDetailsModel import WalletDetails

class WalletDetailsRepository(IWalletDetailsRepository):

    def create(self, body: dict, wallet_id: int, qr: str) -> WalletDetails:
        wallet_details = WalletDetails()
        wallet_details.wallet_id = wallet_id
        wallet_details.network_id = body['network_id']
        wallet_details.address = body['address']
        wallet_details.qr = qr
        wallet_details.save_db()
        return wallet_details

    def get(self, wallet_id: int, network_id: int) -> WalletDetails:
        wallet_detail = WalletDetails.query.filter_by(wallet_id=wallet_id, network_id=network_id).first()
        return wallet_detail
