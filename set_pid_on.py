#!/usr/bin/env python
import omegacn7500
import settings

instrument = omegacn7500.OmegaCN7500(settings.port,settings.rimsaddressint) # port name, slave address
instrument.run()
