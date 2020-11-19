def exp_mod(x, n, m = 10000):
    if x == 0: return 0
    if n == 0: return 1

    u = exp_mod(x, n//2, m)
    u = (u * u) % m

    if n % 2:
        u = (u * x) % m

    return u

