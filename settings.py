#!/usr/bin/env python
#this file is used to store common variables for the adaptibrew configuration
port = "/dev/ttyAMA0"
# this is the address of the PID, which is controlled by the minimalmodbus lib
# than the relays
rimsaddressint = 1
switchaddressint = 2
baudrate = 19200
timeout = 2
MA0 = '55' #master start byte
MA1 = 'AA' #master1 byte
MAE = '77' #master end byte
CN  = '02'  #hex byte for controller number
# these are relay numbers on the STR116 board and a custom to each installation
spargeToMashRelay = 0
spargeRelay = 1
rimsToMashRelay = 2
pumpRelay = 3
DEBUG = False
