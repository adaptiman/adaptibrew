#!/usr/bin/env python
import omegacn7500
import settings

instrument = omegacn7500.OmegaCN7500(settings.port,settings.rimsAddress) # port name, slave address
instrument.run()

print("PID on")
