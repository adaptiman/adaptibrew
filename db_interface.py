import exchange

con = exchange.connect()

# exchange.create_info_table(con)
exchange.insert(con, "info", "pv", "45")
print(exchange.get_info(con))

con.close()
