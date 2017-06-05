import exchange
import time

con = exchange.connect()
exchange.create_info_table(con)

while True:
    exchange.insert(con, "pv", "45")
    print exchange.get_info(con)
    time.sleep(1)


con.close()
