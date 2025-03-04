from src import db
from src.__Parents.Model import Model

class Network(Model, db.Model):
    symbol = db.Column(db.String(10))
    label = db.Column(db.String(60))
    derive_path = db.Column(db.String(20))
    rpc_url = db.Column(db.String(120))
    explorer_url = db.Column(db.String(120))
    chain_id = db.Column(db.String(120))
    background_url = db.Column(db.String(320))
    index = db.Column(db.Integer, default=0)
