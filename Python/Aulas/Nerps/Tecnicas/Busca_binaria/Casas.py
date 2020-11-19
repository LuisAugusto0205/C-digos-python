import bisect
def main():
    n = int(input())
    casas = [int(input()) for _ in range(n)]
    k = int(input())
    for casa1 in casas:
        casa2 = k - casa1
        i = bisect.bisect_left(casas, casa2)
        if casas[i%n] == casa2:
            print('{} {}'.format(min(casa1, casa2), max(casa1, casa2)))
            break
main()
