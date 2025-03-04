from src import db
from src.__Parents.Model import Model

class WalletDetails(Model, db.Model):
    network_id = db.Column(db.Integer, db.ForeignKey('network.id'))
    network = db.relationship('Network')
    address = db.Column(db.String(200))
    wallet_id = db.Column(db.Integer, db.ForeignKey('wallet.id'))
    wallet = db.relationship('Wallet')
    qr = db.Column(db.Text)