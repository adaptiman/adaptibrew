#!/usr/bin/env python
import omegacn7500, settings, json, sys

instrument = omegacn7500.OmegaCN7500(settings.port,settings.rimsAddress) # port name, slave address
json.dump(instrument.is_running(), sys.stdout)
