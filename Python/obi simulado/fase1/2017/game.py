def main():
    n = int(input())
    d = int(input())
    a = int(input())
    print(solve(n, d, a))

def solve(n, d, a):
    if d > a:
        return d - a
    elif d < a:
        return (n - a) + d
    else:
        return 0

main()
