#!/usr/bin/env python
import exchange
from exchange import Info
import time

db = exchange.connect()

if not Info.table_exists():
    db.create_tables([Info])

while True:
    exchange.write_latest_data()
    exchange.check_for_requests()
    time.sleep(0.5)
