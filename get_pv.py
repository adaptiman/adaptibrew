#!/usr/bin/env python
import omegacn7500, settings, time, json, sys

instrument = omegacn7500.OmegaCN7500(settings.port,settings.rimsAddress) # port name, slave address

json.dump(instrument.get_pv(), sys.stdout)
