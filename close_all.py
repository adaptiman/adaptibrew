#!/usr/bin/env python
import serial
import settings

usart = serial.Serial (settings.port,settings.baudRate)
bytestring = "55AA081702000F003077"
message_bytes = bytestring.decode("hex")
usart.write(message_bytes)
