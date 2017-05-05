import str116, sys, json

if str116.get_relay(int(sys.argv[1])):
    json.dump({sys.argv[1]: True}, sys.stdout)
else:
    json.dump({sys.argv[1]: False}, sys.stdout)
    pass
