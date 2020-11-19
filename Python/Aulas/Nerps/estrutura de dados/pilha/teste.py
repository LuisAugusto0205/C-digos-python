def main():
    n, d = map(int, input().split())

    while n > 0 and d > 0:
        num = [(k, i) for i, k in enumerate(input())]
        num.sort()
        num = num[d:]
        print(''.join(map(str, [t[0] for t in sorted(num, key = lambda t: t[1])])))

        n, d = map(int, input().split())

main()
