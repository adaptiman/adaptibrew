import str116
import sys
import settings

str116.set_relay(int(sys.argv[1]), int(sys.argv[2]))

if int(sys.argv[2]) == 1:
    state = "on"
else:
    state = "off"
print("relay " + sys.argv[1] + " " + state)
