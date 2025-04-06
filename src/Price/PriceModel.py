from src import db
from src.__Parents.Model import Model

class Price(Model, db.Model):
    symbol = db.Column(db.String(10))
    usd_price = db.Column(db.String(80))
    change_24h = db.Column(db.String(40))
