def crivo(n):
    tabela = [0]*(n + 1)
    kDivisores = []
    
    R = int(n ** 0.5)
    for i in range(1, R + 1):
        tabela[i * i] += i
        
        for j in range(i*i + i, n + 1, i):
            tabela[j] += i + j//i

    for i in range(1, n + 1):
        tabela[i] += tabela[i - 1]

    return tabela

def main():
    divinos = crivo(1000000)

    n = int(input())
    while n > 0:
        print(divinos[n])
        n = int(input())

main()
