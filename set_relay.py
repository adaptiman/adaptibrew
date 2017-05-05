import str116
import sys
import settings
import json

str116.set_relay(int(sys.argv[1]), int(sys.argv[2]))

if int(sys.argv[2]) == 1:
    state = "on"
else:
    state = "off"
output = "relay " + sys.argv[1] + " " + state

json.dump(output, sys.stdout)
