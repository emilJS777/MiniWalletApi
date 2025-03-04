import logging

from flask import Flask, request, g
from flask_sock import ConnectionClosed
from src.Wallet.WalletMiddleware import WalletMiddleware
from .ISocket import ISocket
from src import sock, app

with app.app_context():
    sids: list = []

with app.app_context():

    class Socket(ISocket):

        @staticmethod
        @sock.route('/')
        def connect(ws):
            logging.info("start ws")
            sids.append(ws)
            try:
                while True:
                    logging.info("receive ws")
                    message = ws.receive()
                    # if message is None:
                    #     break
                    # Handle incoming messages if needed
            except ConnectionClosed as e:
                for sid in sids:
                    if sid == ws:
                        sids.remove(sid)
                        break
                logging.info("error ws")
                logging.error(e)
                # raise e
            finally:
                logging.info("final ws")
                for sid in sids:
                    if sid == ws:
                        sids.remove(sid)
                        break

        def send(self, emit_name: str, data: dict) -> bool:
            for sid in sids:
                sid.send({"topic": emit_name, "data": data})
            return True

