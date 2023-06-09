from loguru import logger
from Large_order.utils import *

request_level = logger.level("FUTURE", no=38, color="<green>")
EXCE = logger.level("EXCE", no=38, color="<blue>")
BIDS_level = logger.level("BIDS", no=38, color="<green>")
ASKS_level = logger.level("ASKS", no=38, color="<red>")
INF_level = logger.level("INF", no=38, color="<yellow>")


class MarketDataDepth:
    ID_stream = 0

    def __init__(self, symbol):
        self.exist_u = False
        self.symbol = symbol
        self.depth_snapshot = {}
        self.last_update_id = None
        self.update_depth_snapshot()
        self.start_stream()

    def get_data(self, volume_USDT):
        try:
            if not self.depth_snapshot:
                return None

            spread_price = float(list(self.depth_snapshot.get('bids').items())[0][0])
            percent_ask = None
            percent_bid = None
            ask_price, ask_volume = None, None
            bid_price, bid_volume = None, None
            ask_volume_usdt, bid_volume_usdt = None, None
            best_most_ask = list(filter(lambda t: float(t[0]) * float(t[1]) >= volume_USDT,
                                        self.depth_snapshot.get('asks').items()))
            if best_most_ask:
                best_most_ask = best_most_ask[0]
                ask_price, ask_volume = tuple(map(float, best_most_ask))
                percent_ask = round((ask_price - spread_price) / spread_price * 100, 1)
                ask_volume_usdt = int(ask_price * ask_volume)

            best_most_bid = list(filter(lambda t: float(t[0]) * float(t[1]) >= volume_USDT,
                                        self.depth_snapshot.get('bids').items()))
            if best_most_bid:
                best_most_bid = best_most_bid[0]
                bid_price, bid_volume = tuple(map(float, best_most_bid))
                percent_bid = round((spread_price - bid_price) / spread_price * 100, 1)
                bid_volume_usdt = int(bid_price * bid_volume)

            res = {
                'best_ask': ask_price,
                'percent_ask': percent_ask,
                'ask_volume': ask_volume,
                'ask_volume_usdt': shorten_number(ask_volume_usdt),
                'best_bid': bid_price,
                'percent_bid': percent_bid,
                'bid_volume': bid_volume,
                'bid_volume_usdt': shorten_number(bid_volume_usdt)
            }
        except Exception as e:
            logger.log("EXCE", f'{self.depth_snapshot} | {e}')
            res = {
                'best_ask': None,
                'percent_ask': None,
                'ask_volume': None,
                'ask_volume_usdt': shorten_number(None),
                'best_bid': None,
                'percent_bid': None,
                'bid_volume': None,
                'bid_volume_usdt': shorten_number(None)
            }
            self.update_depth_snapshot()

        return res

    def update_depth_snapshot(self):
        pass

    def start_stream(self):
        pass
