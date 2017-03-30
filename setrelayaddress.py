#!/usr/bin/env python
import serial
import time
import binascii

data = "55AA08060100024D5E77" #Sets all devices on the bus to address 2
usart = serial.Serial ("/dev/ttyAMA0",19200)
usart.timeout = 2
message_bytes = data.decode("hex")
try:
    usart.write(message_bytes)
    #print usart.is_open  # True for opened
    if usart.isOpen: #old command was usart.is_open, which is python3x style        time.sleep(0.5)
        size = usart.inWaiting()
        if size:
            data = usart.read(size)
            print(binascii.hexlify(data))
        else:
            print('no data')
    else:
        print('usart not open')
except IOError as e :
    print("Failed to write to the port. ({})".format(e))
