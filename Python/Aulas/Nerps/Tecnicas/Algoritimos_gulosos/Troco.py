def main():
    n = int(input())
    print(solve(n))

def solve(n):
    moedas = 0
    while n > 0:
        if n >= 100:
            moedas += n // 100
            n %= 100
        elif n >= 50:
            moedas += 1
            n -= 50
        elif n >= 25:
            moedas += 1
            n -= 25
        elif n >= 10:
            moedas += n // 10
            n %= 10
        elif n >= 5:
            moedas += 1
            n -= 5
        else:
            moedas += n // 1
            n %= 1
    return moedas
main()
