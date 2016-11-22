#!/usr/bin/env python
import serial
import settings
def _write_message(data):
    usart = serial.Serial (settings.port,settings.baudrate)
    message_bytes = data.decode("hex")
    usart.write(message_bytes)
def _get_checksum(data):
    checksum = sum(bytearray.fromhex(data))
    checksumstripped = hex(checksum).replace('0x', '')
    return checksumstripped

def relay_on(relaynumber):
    #command to turn on relay is 0x08 0x17
    #format is
    #MA0, MA1, 0x08, 0x17, CN, start number output (relaynumber), \
    #number of outputs (usually 0x01), 0/1, CS, MAE
    #need to do a checksum on
    #0x08, 0x17, CN, relaynumber, 0x01, 0x01
    relaynumberhex = hex(relaynumber).replace('0x', '').zfill(2)
    str_to_checksum = '0817' + settings.CN + str(relaynumberhex) + '0101'
    CS = _get_checksum(str_to_checksum)
    bytestring = settings.MA0 + settings.MA1 + str_to_checksum + str(CS.zfill(2)) + settings.MAE
    _write_message(bytestring)
