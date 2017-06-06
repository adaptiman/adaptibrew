from peewee import *
import os
from os.path import expanduser

db_dir = expanduser("~/.brewer/db/")
db_file = "exchange.db"
db = SqliteDatabase(db_dir + db_file)

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

    class Meta:
        database = db
