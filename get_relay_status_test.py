#!/usr/bin/env python
import str116, sys, json

json.dump(main(str116.get_relays_status()), sys.stdout)
