#!/usr/bin/env python
import str116
import settings
import sys
import json

str116.set_relay(settings.relays['pump'],1)
json.dump("pump on", sys.stdout)
