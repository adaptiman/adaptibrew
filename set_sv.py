#!/usr/bin/env python
import omegacn7500
import settings
import sys

instrument = omegacn7500.OmegaCN7500(settings.port,settings.rimsAddress)
# port name, slave address

instrument.set_setpoint(float(sys.argv[1]))
json.dump(float(argv[1]), sys.stdout)
# Registernumber, value, number of decimals for storage
