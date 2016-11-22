#!/usr/bin/env python
import binascii

data = '\x08\x17\x02\x10\x01\x01'
checksum = 0
for ch in data:
    checksum += ord(ch)
print checksum, hex(checksum)
