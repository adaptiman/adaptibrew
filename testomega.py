#!/usr/bin/env python
import omegacn7500
#import serial
#import minimalmodbus

instrument = omegacn7500.OmegaCN7500('/dev/ttyAMA0', 1) # port name, slave address
#instrument.serial.baudrate = 19200
#instrument.serial.bytesize = 8
#instrument.serial.parity = serial.PARITY_NONE
#instrument.serial.stopbits = 1
#instrument.serial.timeout = 1.0
#instrument.mode = minimalmodbus.MODE_RTU

print instrument.get_pv() # print temperature
print instrument.get_setpoint()
