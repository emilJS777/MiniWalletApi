from .IPriceRepository import IPriceRepository
from .PriceModel import Price


class PriceRepository(IPriceRepository):
    def create(self, body):
        price = Price()
        price.symbol = body['symbol']
        price.change_24h = body['change_24h']
        price.usd_price = body['usd_price']
        price.save_db()

    def get_all(self) -> list[Price]:
        prices = Price.query.all()
        return prices