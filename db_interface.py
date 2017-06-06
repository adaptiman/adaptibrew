#!/usr/bin/env python
from peewee import *
from os.path import expanduser
from exchange import Info
import exchange
import omegacn7500
import settings
import str116
import time

omega = omegacn7500.OmegaCN7500(settings.port, settings.rimsAddress)

db = exchange.connect()

if not Info.table_exists():
    db.create_tables([Info])

while True:
    info = Info(
        pv = omega.get_pv(),
        sv = omega.get_setpoint(),
        pid_running = omega.is_running(),
        hltToMash = str116.get_relay(settings.relays['hltToMash']),
        hlt = str116.get_relay(settings.relays['hlt']),
        rimsToMash = str116.get_relay(settings.relays['rimsToMash']),
        pump = str116.get_relay(settings.relays['pump'])
    )
    info.save()
    time.sleep(3)
