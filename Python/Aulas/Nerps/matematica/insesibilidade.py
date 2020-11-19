def main():
    n = int(input())

    x1 = y1 = x2 = y2 = 0
    insensibilidade = 0

    for _ in range(n):
        x1, y1, x2, y2 = [int(x) for x in input().split()]
        d = (x1 - x2)**2 + (y1 - y2)**2
        insensibilidade += d

    print(insensibilidade)

main()
