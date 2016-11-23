#!/usr/bin/env python
import serial
import settings
import time
import binascii

def _write_message(data):
    usart = serial.Serial (settings.port,settings.baudrate)
    usart.timeout = settings.timeout
    message_bytes = data.decode("hex")
    try:
        usart.write(message_bytes)
    except IOError as e :
        print("Failed to write to the port. ({})".format(e))

def _write_message_with_response(data):
    usart = serial.Serial (settings.port,settings.baudrate)
    usart.timeout = settings.timeout
    message_bytes = data.decode("hex")
    try:
        usart.write(message_bytes)
#        print usart.is_open  # True for opened
        if usart.is_open:
            time.sleep(0.5)
            size = usart.inWaiting()
            if size:
                data = usart.read(size)
#                print binascii.hexlify(data)
            else:
                print 'no data'
        else:
            print 'usart not open'
    except IOError as e :
        print("Failed to write to the port. ({})".format(e))
    return binascii.hexlify(data)

def _get_checksum(data):
    checksum = sum(bytearray.fromhex(data))
    checksumstripped = hex(checksum).replace('0x', '')
    return checksumstripped.zfill(2)

def set_relay(relaynumber, onoff):
    #command to turn on relay is 0x08 0x17
    #format is
    #MA0, MA1, 0x08, 0x17, CN, start number output (relaynumber), \
    #number of outputs (usually 0x01), 00/01 (off/on), CS (calculated), MAE
    #need to do a checksum on 0x08, 0x17, CN, relaynumber, 0x01, 0x01
    relaynumberhex = hex(relaynumber).replace('0x', '').zfill(2)
    str_to_checksum = '0817' + settings.CN + str(relaynumberhex) \
        + '01' + str(onoff).zfill(2)
    CS = _get_checksum(str_to_checksum)
    bytestring = settings.MA0 + settings.MA1 + str_to_checksum \
        + str(CS) + settings.MAE
    print('set_relay bytestring: ' + bytestring)
    _write_message(bytestring)

def get_relay_status():
    #command to get the status of all of the relays in an array.
    #format is
    #MA0, MA1, 0x07, 0x14, CN, start number output, number of outputs, CS, MAE
    #returns
    #SL0, SL1, BC, output first, output next,..., CS, SLE
    str_to_checksum = '0714' + settings.CN + '0010'
    CS = _get_checksum(str_to_checksum)
    bytestring = settings.MA0 + settings.MA1 + str_to_checksum \
        + str(CS) + settings.MAE
    print('relay status bytestring: ' + bytestring)
    relaystatus = _write_message_with_response(bytestring)[6:-4]
    print('relay status: ' + relaystatus)
