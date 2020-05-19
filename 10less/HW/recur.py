def recur(n):
    a = 2
    if n == 0:
        return 1
    r = recur(n - 1)
    return a * r
