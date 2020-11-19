def main():
    n, k = [int(x) for x in input().split()]
    while n > 0 or k > 0:
        Max = n
        Min = n
        for i in range(k):
            p = [int(x) for x in input().split()]
            b = [0, 0]

            for i, num in enumerate([n & (1 << p[0]),
                                    n & (1 << p[1])]):
                if num:
                    b[i] = 1
                    

            if b[1] != b[0]:
                n ^= (1 << p[0])
                n ^= (1 << p[1])

            Max = max(Max, n)
            Min = min(Min, n)

        print(n, end = ' ')
        print(Max, end = ' ')
        print(Min)

        n, k = [int(x) for x in input().split()]

main()
