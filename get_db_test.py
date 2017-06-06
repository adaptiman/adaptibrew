import exchange
from exchange import Info

db = exchange.connect()

while True:
    info = Info.get()
    print info.pv
