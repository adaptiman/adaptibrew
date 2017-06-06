#!/usr/bin/env python
import serial
import time

port = "/dev/ttyAMA0"
usart = serial.Serial (port,9600)
bytestring = "55AA083302AA55064277" #set baudrate to 19200
message_bytes = bytestring.decode("hex")
usart.write(message_bytes)
