#!/usr/bin/env python
import exchange
from exchange import Info
from exchange import Request
from peewee import *
import time

db = exchange.connect()

if not Info.table_exists():
    db.create_tables([Info])

if not Request.table_exists():
    db.create_tables([Request])

# request = Request(
#     method = "set_sv",
#     args = "140",
#     timestamp = time.time()
# )
# exchange.execute(request.method, request.args)

while True:
    exchange.write_latest_data()
    exchange.check_for_requests()
    time.sleep(0.5)
