import str116
import sys

if str116.get_relay(int(sys.argv[1])):
    print("relay 0" + sys.argv[1] + ": on")
else:
    print("relay 0" + sys.argv[1] + ": off")
    pass
