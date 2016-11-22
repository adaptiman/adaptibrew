#!/usr/bin/env python

data = '0817020F0101'
checksum = sum(bytearray.fromhex(data))
print hex(checksum)
checksumstripped = hex(checksum).replace('0x', '')
print checksumstripped
