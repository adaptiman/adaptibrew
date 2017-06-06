#!/usr/bin/env python
import exchange
from exchange import Info
from exchange import Request
import time

db = exchange.connect()

if not Info.table_exists():
    db.create_tables([Info])

if not Request.table_exists():
    db.create_tables([Request])

while True:
    exchange.write_latest_data()   # Get data from hardware and write it to db
    exchange.check_for_requests()  # Check for new requests

    # Checking for new requests takes about 0.003 seconds; not an issue.
    # Writing the data takes about 2-3 seconds, since gathering the data from the hardware
    # (i.e. minimalmodbus) takes a long time
