from .NetworkService import NetworkService
from src.__Parents.Controller import Controller
from .NetworkRepository import NetworkRepository

class NetworkController(Controller):
    network_service = NetworkService(NetworkRepository())

    def post(self):
        res: dict = self.network_service.create(body=self.request.get_json())
        return res

    def put(self):
        res: dict = self.network_service.update(network_id=self.arguments.get('id'), body=self.request.get_json())
        return res

    def delete(self):
        res: dict = self.network_service.delete(network_id=self.arguments.get('id'))
        return res

    def get(self):
        if(self.arguments.get('id')):
            res: dict = self.network_service.get_by_id(network_id=self.arguments.get('id'))
        else:
            res: dict = self.network_service.get_all()
        return res
