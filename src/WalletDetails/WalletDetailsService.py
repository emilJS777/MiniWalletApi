import base64
import io
from .IWalletDetailsRepository import IWalletDetailsRepository
from ..Price.IPriceRepository import IPriceRepository
from ..Price.PriceService import PriceService
from ..Token.ITokenRepository import ITokenRepository
from ..__Parents.Rosponse import Response
from flask import g, request
import os
import requests
import qrcode

class WalletDetailsService(Response):
    def __init__(self, wallet_details_repository: IWalletDetailsRepository, token_repository: ITokenRepository, price_repository: IPriceRepository):
        self.wallet_details_repository: IWalletDetailsRepository = wallet_details_repository
        self.token_repository: ITokenRepository = token_repository
        self.price_service = PriceService()
        self.price_repository = price_repository

    def create_qr(self, address: str):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=5,
            border=2,
        )
        qr.add_data(address)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        return img_base64

    def create(self, body: dict) -> dict:
        qr = self.create_qr(address=body["address"])
        self.wallet_details_repository.create(body=body, wallet_id=g.wallet.id, qr=qr)
        return self.response_created()

    def get_details(self, network_id: int) -> dict:
        wallet_detail = self.wallet_details_repository.get(wallet_id=g.wallet.id, network_id=network_id)
        prices = self.price_repository.get_all()

        if not wallet_detail:
            return self.response_not_found()
        tokens = self.token_repository.get_all_by_network_id(network_id=network_id)

        try:
            token_details = []
            # external_price_table = self.price_service.get_price_table()
            for token in tokens:
                response = requests.get(f"{os.environ.get('COIN_WRAPPER_URL')}/balance?symbol={token.network.symbol}&address={wallet_detail.address}&contract_address={token.contract_address}")
                usd_price = next((p.usd_price for p in prices if p.symbol == token.symbol), "0")
                change_24_h = next((p.change_24h for p in prices if p.symbol == token.symbol), "0")
                token_details.append({"id": token.id, "network_symbol": token.network.symbol, "native": token.native, "symbol": token.symbol, "balance": str(response.json()['obj']['balance']), 'label': token.label, "usd_price": usd_price, "change_24h": change_24_h})
        except Exception as e:
            return self.response_err_msg(str(e))

        return self.response_ok({
            "id": wallet_detail.id,
            "network_id": wallet_detail.network_id,
            "network": {
                'id': wallet_detail.network.id,
                'symbol': wallet_detail.network.symbol,
                'label': wallet_detail.network.label,
                'derive_path': wallet_detail.network.derive_path,
                'rpc_url': wallet_detail.network.rpc_url,
                'explorer_url': wallet_detail.network.explorer_url,
                'chain_id': wallet_detail.network.chain_id,
            },
            "address": wallet_detail.address,
            "wallet_id": wallet_detail.wallet_id,
            "tokens": token_details,
            "qr": wallet_detail.qr,
        })