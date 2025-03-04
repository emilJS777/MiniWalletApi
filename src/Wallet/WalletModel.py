from src import db
from src.__Parents.Model import Model

class Wallet(Model, db.Model):
    hash = db.Column(db.String(600))
