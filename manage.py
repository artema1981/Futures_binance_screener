#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from redis_db import redis_client
from Large_order.symbols import all_futures_binance
from market_data.instans_lists import all_book_depth, create_RDB_list
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Futures_binance_screener.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)




if __name__ == '__main__':
    redis_client.flushall()
    all_futures_binance()
    all_book_depth()
    # create_RDB_list()
    main()
