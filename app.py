import asyncio
import threading

from src import app
from src.Price.PriceRepository import PriceRepository
from src.Socket.Socket import Socket
from src.Updater.UpdaterService import UpdaterService
from src.Token.TokenRepository import TokenRepository
from src.Price.PriceService import PriceService
from flask import current_app

if __name__ == '__main__':
    # with app.app_context():
    #     Socket()

    # with app.app_context():
    #     updater_service = UpdaterService(token_repository=TokenRepository(), socket=Socket())
    #     start_updater_in_thread = updater_service.start_price_updated()
    #     updater_thread = threading.Thread(target=start_updater_in_thread)
    #     updater_thread.start()
    with app.app_context():
        def thread_function():
            with app.app_context():
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                updater_service = UpdaterService(token_repository=TokenRepository(), socket=Socket(), price_repository=PriceRepository())
                loop.run_until_complete(updater_service.start_price_updated())
        #
        # def thread_function2():
        #     with app.app_context():
        #         loop = asyncio.new_event_loop()
        #         asyncio.set_event_loop(loop)
        #         updater_service = UpdaterService(token_repository=TokenRepository(), socket=Socket())
        #         loop.run_until_complete(updater_service.start_fee_updated())

        # Start the listener thread
        listener_thread = threading.Thread(target=thread_function)
        listener_thread.start()

        # listener_thread2 = threading.Thread(target=thread_function2)
        # listener_thread2.start()

    print("app run")
    app.run(debug=True)
