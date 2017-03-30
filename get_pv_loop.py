#!/usr/bin/env python
import omegacn7500
import settings
import time

instrument = omegacn7500.OmegaCN7500(settings.port,settings.rimsaddressint) # port name, slave address

while True:
	print instrument.get_pv() # print temperature
	time.sleep(5)
