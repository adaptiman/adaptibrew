#!/usr/bin/env python
import omegacn7500
import settings

instrument = omegacn7500.OmegaCN7500(settings.port,settings.rimsaddressint)
# port name, slave address

instrument.write_register(24,58, 1) 
# Registernumber, value, number of decimals for storage
