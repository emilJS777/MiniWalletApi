from .TokenService import TokenService
from src.__Parents.Controller import Controller
from .TokenRepository import TokenRepository

class TokenController(Controller):
    token_service = TokenService(TokenRepository())

    def post(self):
        res: dict = self.token_service.create(body=self.request.get_json())
        return res

    def put(self):
        res: dict = self.token_service.update(token_id=self.arguments.get('id'), body=self.request.get_json())
        return res

    def delete(self):
        res: dict = self.token_service.delete(token_id=self.arguments.get('id'))
        return res

    def get(self):
        if(self.arguments.get('id')):
            res: dict = self.token_service.get_by_id(token_id=self.arguments.get('id'))
        else:
            res: dict = self.token_service.get_all()
        return res
