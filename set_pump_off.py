#!/usr/bin/env python
import str116
import settings
import sys
import json

str116.set_relay(settings.relays['pump'],0)
json.dump("pump off", sys.stdout)
