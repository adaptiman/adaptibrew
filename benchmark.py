import exchange
import omegacn7500
import time
import sys
import settings
import str116

omega = omegacn7500.OmegaCN7500(settings.port, settings.rimsAddress)

def write_data_to_db():
    exchange.write_latest_data()

def read_request_from_db():
    exchange.check_for_requests()

# Used to take ~2 seconds
def get_data_for_sqlite():
    pv = omega.get_pv(),
    sv = omega.get_setpoint(),
    pid_running = omega.is_running(),
    hltToMash = str116.get_relay(settings.relays['hltToMash']),
    hlt = str116.get_relay(settings.relays['hlt']),
    rimsToMash = str116.get_relay(settings.relays['rimsToMash']),
    pump = str116.get_relay(settings.relays['pump']),
    timestamp = time.time(),


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("read_request_from_db()", setup="from __main__ import read_request_from_db", number=1))
