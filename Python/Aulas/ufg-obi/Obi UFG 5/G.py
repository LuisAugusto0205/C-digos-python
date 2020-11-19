def main():
    n = int(input())
    print(solve(n))

def solve(n):
    ganhou = 0
    for _ in range(n):
        carro = int(input())
        if carro != 1:
            ganhou += 1
    return ganhou

main()
