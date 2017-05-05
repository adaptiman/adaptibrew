#!/usr/bin/env python
import omegacn7500
import settings
import sys
import json

instrument = omegacn7500.OmegaCN7500(settings.port,settings.rimsAddress) # port name, slave address
instrument.run()

json.dump("PID on", sys.stdout)
