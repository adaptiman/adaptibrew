#!/usr/bin/env python
import omegacn7500
import settings
import sys

instrument = omegacn7500.OmegaCN7500(settings.port,settings.rimsaddressint)
# port name, slave address

instrument.set_setpoint(int(sys.argv[1])) 
# Registernumber, value, number of decimals for storage
