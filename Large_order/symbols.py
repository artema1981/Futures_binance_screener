from redis_db import *

from binance.um_futures import UMFutures


def all_futures_binance():

    """
    Api futures binance_futures.
    set to redis db list of dict coins data
    """
    um_futures_client = UMFutures()
    res = um_futures_client.exchange_info()
    all_futures_symbols = []
    for i in res['symbols']:
        if i['status'] == 'TRADING' and \
                i['contractType'] == 'PERPETUAL' and \
                i['underlyingType'] == 'COIN' and \
                i['quoteAsset'] == 'USDT':
            all_futures_symbols.append(i)
    set_redis(name='all_futures_binance', value=all_futures_symbols)
