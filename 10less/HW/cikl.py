def cikl(n):
    a = 2
    r = range(1, n)
    total = 1
    for _ in r:
        total *= a
    return total
