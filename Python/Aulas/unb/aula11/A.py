def main():
    n = int(input())
    print(solve(n))

def solve(n):
    res = 0
    for _ in range(n):
        st = input()
        if '+' in st:
            res += 1
        else:
            res -= 1
    return res
main()
