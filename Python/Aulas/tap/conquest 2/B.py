def crivo(k):
    primos = [True]*(k + 1)
    primos[0] = primos[1] = False
    
    for i in range(4, k + 1, 2):
        primos[i] = False

    r = int(round(k ** 0.5 + 0.5, 0))
    for i in range(3, r + 1, 2):
        if primos[i]:
            for j in range(i * i, k + 1, i):
                primos[j] = False

    p_lista = []
    for i in range(2, k + 1):
        if primos[i]:
            p_lista.append(i)

    return p_lista, primos

def main():
    primos, tabela = crivo(1000000)
    n = int(input())
    
    while n > 0:
        for p in primos:
            if tabela[n - p]:
                k = n - p
                break

        print('{} = {} + {}'.format(n, p, k))
        n = int(input())

main()
