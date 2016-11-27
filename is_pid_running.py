#!/usr/bin/env python
import omegacn7500
import settings
import time

print(settings.rimsaddressint)
instrument = omegacn7500.OmegaCN7500(settings.port,settings.rimsaddressint) # port name, slave address
instrument.is_running
