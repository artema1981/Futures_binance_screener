from .spotdepth_class import SpotDepth
from .futuredepht_class import FutureDepth
from redis_db import *
import time

spot_obj_list = []
future_obj_list = []


def all_book_depth():
    symbols = json.loads(get_redis('all_futures_binance'))
    symbols_future = [d.get('symbol') for d in symbols]
    symbols_spot = []
    for i in symbols_future:
        if i[:4] == '1000':
            symbols_spot.append(i[4:])
        elif i == 'LUNA2USDT':
            symbols_spot.append('LUNAUSDT')
        else:
            symbols_spot.append(i)
    for i in range(len(symbols_spot)):
        spot_obj_list.append(SpotDepth(symbols_spot[i]))
        future_obj_list.append(FutureDepth(symbols_future[i]))
        time.sleep(0.5)
