# This is about to go away probably


import exchange
import time
import omegacn7500
import settings
import str116

# pv
# instrument.get_pv()

# sv
# WHY IS THIS NAMED LIKE THIS UGH ???
# instrument.get_setpoint()

# is pid running?
# instrument.is_running()

# Relay status
# str116.get_relays_status()

instrument = omegacn7500.OmegaCN7500(settings.port, settings.rimsAddress)
exchange.delete_db
con = exchange.connect()

exchange.create_info_table(con)

while True:
    exchange.insert(con, "pv", instrument.get_pv())
    exchange.insert(con, "sv", instrument.get_setpoint())
    exchange.insert(con, "pid_running", instrument.is_running())
    # exchange.insert(con, "", instrument.get_pv())
    time.sleep(1)
    print exchange.get_info(con)

con.close()
