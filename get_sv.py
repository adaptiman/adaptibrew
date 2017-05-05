#!/usr/bin/env python
import omegacn7500
import settings
import time

instrument = omegacn7500.OmegaCN7500(settings.port,settings.rimsAddress) # port name, slave address

print instrument.get_setpoint() # print temperature
