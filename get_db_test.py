import exchange
from exchange import Info

db = exchange.connect()

info = Info.get()
print info.pv
