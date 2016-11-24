#!/usr/bin/env python
import serial
import time
import settings

usart = serial.Serial (settings.port,settings.baudrate)
bytestring = "55AA0817020008012A77"
message_bytes = bytestring.decode("hex")
usart.write(message_bytes)
time.sleep(5)
message_bytes = "55AA0817020008002977".decode("hex")
usart.write(message_bytes)
