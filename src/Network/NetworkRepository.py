from operator import index

from .INetworkRepository import INetworkRepository
from src.Network.NetworkModel import Network

class NetworkRepository(INetworkRepository):

    def create(self, body: dict):
        network = Network()
        network.symbol = body['symbol']
        network.label = body['label']
        network.derive_path = body['derive_path']
        network.rpc_url = body['rpc_url']
        network.explorer_url = body['explorer_url']
        network.chain_id = body['chain_id']
        network.background_url = body['background_url']
        network.index = body['index']
        network.save_db()

    def update(self, network: Network, body: dict):
        network.symbol = body['symbol']
        network.label = body['label']
        network.derive_path = body['derive_path']
        network.rpc_url = body['rpc_url']
        network.explorer_url = body['explorer_url']
        network.chain_id = body['chain_id']
        network.background_url = body['background_url']
        network.index = body['index']
        network.update_db()

    def delete(self, network: Network):
        network.delete_db()

    def get_by_id(self, network_id) -> Network:
        network = Network.query.filter_by(id=network_id).first()
        return network

    def get_all(self) -> list[Network]:
        networks = Network.query.order_by(Network.index).all()
        return networks
