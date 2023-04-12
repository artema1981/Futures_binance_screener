from loguru import logger

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

    def update_depth_snapshot(self):
        pass

    def start_stream(self):
        pass

