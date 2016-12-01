#!/usr/bin/env python
import omegacn7500
import settings

instrument = omegacn7500.OmegaCN7500(settings.port,settings.rimsaddressint)
# port name, slave address

instrument.set_setpoint(44.6) 
# Registernumber, value, number of decimals for storage
