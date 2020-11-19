def main():
    a, b, x, y = [int(z) for z in input().split()]
    print(solve(a, b, x, y))

def solve(a, b, x, y):
    div =  mdc(x, y)
    x //= div
    y //= div
    return min(a//x, b//y)

def mdc(n, d):
    if n == 0: return d
    if d == 0: return n
    while n % d > 0:
        n, d = d, n%d
    return d

main()
