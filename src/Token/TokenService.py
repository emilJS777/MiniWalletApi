from src.__Parents.Rosponse import Response
from .ITokenRepository import ITokenRepository

class TokenService(Response):
    def __init__(self, token_repository: ITokenRepository):
        self.token_repository = token_repository

    def create(self, body: dict) -> dict:
        self.token_repository.create(body)
        return self.response_created()

    def update(self, token_id: int, body: dict) -> dict:
        token = self.token_repository.get_by_id(token_id)
        if not token:
            return self.response_not_found()
        self.token_repository.update(token, body)
        return self.response_updated()

    def delete(self, token_id: int) -> dict:
        token = self.token_repository.get_by_id(token_id)
        if not token:
            return self.response_not_found()
        self.token_repository.delete(token)
        return self.response_deleted()

    def get_by_id(self, token_id: int = None) -> dict:
        token = self.token_repository.get_by_id(token_id)
        if not token:
            return self.response_not_found()
        return self.response_ok({
            'id': token.id,
            'symbol': token.symbol,
            'label': token.label,
            'native': token.native,
            'contract_address': token.contract_address,
            'network_id': token.network_id,
            "index": token.index,
            "price_key": token.price_key,
            "gas_limit": token.gas_limit,
            'network': {
                'id': token.network.id,
                'symbol': token.network.symbol,
                'label': token.network.label,
                'derive_path': token.network.derive_path,
                'rpc_url': token.network.rpc_url,
                'explorer_url': token.network.explorer_url,
                'chain_id': token.network.chain_id,
            } if token.network else None
        })

    def get_all(self) -> dict:
        tokens = self.token_repository.get_all()
        return self.response_ok([{
            'id': token.id,
            'symbol': token.symbol,
            'label': token.label,
            'native': token.native,
            'contract_address': token.contract_address,
            'network_id': token.network_id,
            "index": token.index,
            "price_key": token.price_key,
            "gas_limit": token.gas_limit,
            'network': {
                'id': token.network.id,
                'symbol': token.network.symbol,
                'label': token.network.label,
                'derive_path': token.network.derive_path,
                'rpc_url': token.network.rpc_url,
                'explorer_url': token.network.explorer_url,
                'chain_id': token.network.chain_id,
            } if token.network else None
        } for token in tokens])
