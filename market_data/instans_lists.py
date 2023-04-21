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
    for i in symbols_future[0:6]:
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


class RenderDataBooks:

    def __init__(self, s_inst: SpotDepth, f_inst: FutureDepth, volume_USDT):
        self.s_inst = s_inst
        self.f_inst = f_inst
        self.volume_USDT =volume_USDT

    def get_unit_data(self):
        return {'symbol': self.s_inst.symbol, 'spot': self.s_inst.get_data(self.volume_USDT), 'future': self.f_inst.get_data(self.volume_USDT)}

# RDB_list=[]
def create_RDB_list(volume_USDT):
    RDB_list = [RenderDataBooks(*t, volume_USDT) for t in list(zip(spot_obj_list, future_obj_list))]
    return RDB_list

