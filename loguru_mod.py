from loguru import logger

GREEN_level = logger.level("GREEN", no=38, color="<green>")
RED_level = logger.level("RED", no=38, color="<red>")
YELLOW_level = logger.level("YELLOW", no=38, color="<yellow>")
request_level = logger.level("FUTURE", no=38, color="<green>")
EXCE = logger.level("EXCE", no=38, color="<blue>")
BIDS_level = logger.level("BIDS", no=38, color="<green>")
ASKS_level = logger.level("ASKS", no=38, color="<red>")
INF_level = logger.level("INF", no=38, color="<yellow>")