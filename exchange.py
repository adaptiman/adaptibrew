from peewee import *
import os
from os.path import expanduser
import omegacn7500
import settings
import str116
import time



db_dir = expanduser("~/.brewer/db/")
db_file = "exchange.db"
db = SqliteDatabase(db_dir + db_file)
omega = omegacn7500.OmegaCN7500(settings.port, settings.rimsAddress)


def connect():
    create_brewer_dir()
    create_db_dir()
    db.connect()
    return db

def create_brewer_dir():
    brewer_dir = expanduser("~") + "/.brewer/"
    if not os.path.exists(brewer_dir):
        os.makedirs(brewer_dir)

def create_db_dir():
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)

def delete_db():
    if os.path.isfile(db_dir + db_file):
        os.remove(db_dir + db_file)
        return True
    else:
        return False

class Info(Model):
    pv = DecimalField()
    sv = DecimalField()
    pid_running = BooleanField()
    hltToMash = BooleanField()
    hlt = BooleanField()
    rimsToMash = BooleanField()
    pump = BooleanField()
    timestamp = DecimalField()
    is_request = BooleanField()
    request = CharField()
    args = CharField()

    class Meta:
        database = db

def write_latest_data():
    info = Info(
        pv=omega.get_pv(),
        sv=omega.get_setpoint(),
        pid_running=omega.is_running(),
        hltToMash=str116.get_relay(settings.relays['hltToMash']),
        hlt=str116.get_relay(settings.relays['hlt']),
        rimsToMash=str116.get_relay(settings.relays['rimsToMash']),
        pump=str116.get_relay(settings.relays['pump']),
        timestamp=time.time(),
        is_request = False
    )
    info.save()


def check_for_requests():
    info = Info.get(Info.is_request == True)
    if time.time() - 3 < info.timestamp:
        # Execute request
