from src.__Parents.Rosponse import Response
from .INetworkRepository import INetworkRepository

class NetworkService(Response):
    def __init__(self, network_repository: INetworkRepository):
        self.network_repository = network_repository

    def create(self, body: dict) -> dict:
        self.network_repository.create(body)
        return self.response_created()

    def update(self, network_id: int, body: dict) -> dict:
        network = self.network_repository.get_by_id(network_id)
        if not network:
            return self.response_not_found()
        self.network_repository.update(network, body)
        return self.response_updated()

    def delete(self, network_id: int) -> dict:
        network = self.network_repository.get_by_id(network_id)
        if not network:
            return self.response_not_found()
        self.network_repository.delete(network)
        return self.response_deleted()

    def get_by_id(self, network_id: int = None) -> dict:
        network = self.network_repository.get_by_id(network_id)
        if not network:
            return self.response_not_found()
        return self.response_ok({
            'id': network.id,
            'symbol': network.symbol,
            'label': network.label,
            'derive_path': network.derive_path,
            'rpc_url': network.rpc_url,
            'explorer_url': network.explorer_url,
            'chain_id': network.chain_id,
        })

    def get_all(self) -> dict:
        networks = self.network_repository.get_all()
        return self.response_ok([{
            'id': network.id,
            'symbol': network.symbol,
            'label': network.label,
            'derive_path': network.derive_path,
            'rpc_url': network.rpc_url,
            'explorer_url': network.explorer_url,
            'chain_id': network.chain_id,
            "background_url": network.background_url
        } for network in networks])
