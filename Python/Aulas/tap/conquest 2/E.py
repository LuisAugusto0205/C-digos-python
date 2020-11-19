def main():
    n = int(input())

    k = int((2*10**9)**0.5)
    primos = crivo(k)
    
    while n > 0:
        n_div = n_divisores(primos, n)
        resp = n_div // 2
        print('{} {}'.format(n, resp))

        n = int(input())
    
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

    return p_lista

def n_divisores(primos, n):
    div = 1
    i = 0
    p = primos[i]
    
    while p * p <= n:
        e = 0
        while n % p == 0:
            n /= p
            e += 1
        i += 1
        p = primos[i]
        div *= (e + 1)

    if n > 1: div *= 2

    return div
            
