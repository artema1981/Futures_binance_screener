from .base_class import MarketDataDepth
import requests
from binance.websocket.um_futures.websocket_client import UMFuturesWebsocketClient
from loguru import logger

my_client = UMFuturesWebsocketClient()
my_client.start()


class FutureDepth(MarketDataDepth):

    def __init__(self, symbol):
        super().__init__(symbol)
        self.U = None
        self.u = 0
        self.pu = None
        self.restart_counter = 0
        self.snapshot_update_counter = 0

    def update_depth_snapshot(self):
        message = requests.get(f"https://fapi.binance.com/fapi/v1/depth?symbol={self.symbol}&limit=1000").json()
        message['asks'] = dict(message['asks'])
        message['bids'] = dict(message['bids'])
        self.last_update_id = int(message.get('lastUpdateId'))
        self.depth_snapshot = message

    def message_handler(self, message):
        print(message)

        if message.get('e') == "depthUpdate":
            self.U = int(message["U"])
            self.pu = int(message["pu"])

            if self.exist_u and not self.u == self.pu:
                logger.log("INF",
                           f"{self.__class__} - {self.snapshot_update_counter}, 'self.update_depth_snapshot()',{self.symbol}, U:{self.U}, u:{self.u}")
                if self.snapshot_update_counter < 5:
                    self.update_depth_snapshot()
                    self.snapshot_update_counter += 1
            self.depth_snapshot['asks'].update(message['a'])
            self.depth_snapshot['bids'].update(message['b'])
            f1 = list(filter(lambda key: float(self.depth_snapshot['asks'][key]) == 0, self.depth_snapshot['asks']))
            f2 = list(filter(lambda key: float(self.depth_snapshot['bids'][key]) == 0, self.depth_snapshot['bids']))
            if f1:
                for i in f1:
                    del self.depth_snapshot['asks'][i]
            if f2:
                for i in f2:
                    del self.depth_snapshot['bids'][i]
            self.u = int(message["u"])
            self.exist_u = True


            # print(self.depth_snapshot)

        if self.symbol == 'BTCUSDT':
            logger.log("ASKS", f"{self.symbol}, asks, {self.depth_snapshot['asks']}")
            logger.log("BIDS", f"{self.symbol}, bids, {self.depth_snapshot['bids']}")

    def start_stream(self):
        my_client.diff_book_depth(
            symbol=self.symbol,
            speed=1000,
            id=self.ID_stream,
            callback=self.message_handler,
        )
