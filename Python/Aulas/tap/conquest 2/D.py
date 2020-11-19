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

def square_free(primos, n):
    fat = []
    i = 0
    p = primos[i]
    
    while p * p <= n:
        while n % p == 0:
            n /= p
            if len(fat) > 0 and fat[-1] == p:
                return 0
            fat.append(p)   
        i += 1
        p = primos[i]

    if n > 1:
        if len(fat) == 0: return -1
        fat.append(p)
    
    if len(fat) % 2 == 0: return 1
    else: return -1

def main():
    primos = crivo(1000)
    mu = [0, 1]
    m = [0, 1]
    
    n = int(input())
    while n > 0:
        if n > len(mu) - 1:
            for i in range(len(mu), n + 1):
                mu.append(square_free(primos, i))
                m.append(m[-1] + mu[-1])

            print('{:>8}{:>8}{:>8}'.format(n, mu[n], m[n]))
        else:
            print('{:>8}{:>8}{:>8}'.format(n, mu[n], m[n]))

        n = int(input())

main()
    
    
