def ack(m, n):
    if not isinstance(n, int):
        print("n should be an integer.")
    elif not isinstance(m, int):
        print("m should be an integer.")
    elif m < 0 or n < 0:
        print("m and n should be positive integers.")
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))


print(ack(1, 0))
