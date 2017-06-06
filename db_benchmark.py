import exchange

def test():
    exchange.write_latest_data()
    # exchange.check_for_requests()


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test", number=1))
