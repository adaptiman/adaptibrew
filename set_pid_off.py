#!/usr/bin/env python
import omegacn7500
import settings
import json
import sys

instrument = omegacn7500.OmegaCN7500(settings.port, settings.rimsAddress) # port name, slave address
try:
    instrument.stop()
except:
    raise

json.dump('PID off', sys.stdout)
