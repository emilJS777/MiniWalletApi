from src import db
from src.__Parents.Model import Model

class Token(Model, db.Model):
    symbol = db.Column(db.String(10))
    label = db.Column(db.String(60))
    native = db.Column(db.Boolean, default=False)
    contract_address = db.Column(db.String(120))
    network_id = db.Column(db.Integer, db.ForeignKey('network.id'))
    network = db.relationship('Network')
    index = db.Column(db.Integer, default=0)
    price_key = db.Column(db.String(30))
    gas_limit = db.Column(db.Integer)
