import sqlite3
import os
from os.path import expanduser

db_dir = expanduser("~") + "/.brewer/db/"
db_file = "exchange.db"

def connect():
    create_brewer_dir()
    create_db_dir()
    con = sqlite3.connect(db_dir + db_file)
    return con.cursor()

def create_db_dir():
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)

def create_brewer_dir():
    brewer_dir = expanduser("~") + "/.brewer/"
    if not os.path.exists(brewer_dir):
        os.makedirs(brewer_dir)

def create_info_table(con):
    return con.execute("CREATE TABLE IF NOT EXISTS info(pv INT NOT NULL);")

def get_info(con):
    con.execute("SELECT * FROM info;")
    return con.fetchall()

def insert(con, table, column, value):
    con.execute("INSERT INTO {} ({}) VALUES ({});".format(table, column, value))

