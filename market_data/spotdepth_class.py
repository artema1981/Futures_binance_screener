import threading
import websocket
import json
from loguru import logger
import requests
from .base_class import MarketDataDepth


class SpotDepth(MarketDataDepth):
    ID_stream = 1000

    def __init__(self, symbol):
        super().__init__(symbol)
        self.U = None
        self.u = 0
        self.pu = None
        self.restart_counter = 0
        self.snapshot_update_counter = 0


    def start_stream(self):
        def on_message(ws, message):
            message = json.loads(message)
            if message.get('e') == "depthUpdate":
                self.U = int(message["U"])
                if self.exist_u and not self.u + 1 == self.U:
                    logger.log("INF",
                               f"{self.__class__} - {self.snapshot_update_counter}, 'self.update_depth_snapshot()',{self.symbol}, U:{self.U}, u:{self.u}")
                    if self.snapshot_update_counter < 5:
                        self.update_depth_snapshot()
                        self.snapshot_update_counter += 1
                self.depth_snapshot['asks'].update(message['a'])
                self.depth_snapshot['bids'].update(message['b'])
                f1 = list(
                    filter(lambda key: float(self.depth_snapshot['asks'][key]) == 0, self.depth_snapshot['asks']))
                f2 = list(
                    filter(lambda key: float(self.depth_snapshot['bids'][key]) == 0, self.depth_snapshot['bids']))
                if f1:
                    for i in f1:
                        del self.depth_snapshot['asks'][i]
                if f2:
                    for i in f2:
                        del self.depth_snapshot['bids'][i]
                self.u = int(message["u"])
                self.exist_u = True


                # if self.symbol == 'ZILUSDT':
                #     logger.log("ASKS", f"{self.symbol}, asks, {self.depth_snapshot['asks']}")
                #     logger.log("BIDS", f"{self.symbol}, bids, {self.depth_snapshot['bids']}")

        def on_error(ws, error):
            self.exist_u = False
            self.U = None
            self.u = 0
            if isinstance(error, TypeError):
                self.restart_counter += 1
                self.start_stream()
                logger.log("INF",
                           f"RESTART: {self.symbol} | , restart_counter: {self.restart_counter} | on_error: {error}")

        def on_close(ws):
            print("### closed ###")

        def on_open(ws):
            params = {
                "method": "SUBSCRIBE",
                "params": [
                    self.symbol.lower() + "@depth@1000ms"
                ],
                "id": self.ID_stream
            }
            ws.send(json.dumps(params))
            SpotDepth.ID_stream += 1

        def start_websocket():
            try:
                websocket.enableTrace(False)
                ws = websocket.WebSocketApp("wss://stream.binance.com:9443/ws",
                                            header=[str(self.ID_stream), self.symbol],
                                            on_message=on_message,
                                            on_error=on_error,
                                            on_close=on_close)
                ws.on_open = on_open
                ws.run_forever()
            except:
                logger.log('INF', f" start_websocket_ERROR {self.symbol}")

        thread = threading.Thread(target=start_websocket)
        thread.start()

        return on_message

    def update_depth_snapshot(self):
        message_spot = requests.get(f"https://api.binance.com/api/v3/depth?symbol={self.symbol}&limit=1000").json()
        try:
            message_spot['asks'] = dict(message_spot['asks'])
            message_spot['bids'] = dict(message_spot['bids'])
            self.last_update_id = int(message_spot.get('lastUpdateId'))
            self.depth_snapshot = message_spot
        except:
            logger.log('INF', f"EXCEPT update_depth_snapshot.  {self.symbol}, {message_spot}")
