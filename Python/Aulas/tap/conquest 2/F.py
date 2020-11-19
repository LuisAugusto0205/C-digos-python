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

def lpd(primos, n):
    fat = []
    i = 0
    p = primos[i]
    if n == 1: return -1
    while p * p <= n:
        while n % p == 0:
            n /= p
            if len(fat) == 0 or fat[-1] != p:
                fat.append(p)   
        i += 1
        p = primos[i]

    if n > 1:
        if len(fat) == 0: return -1
        fat.append(p)
    return fat[-1]

def main():
    n = int(input())
    primos = crivo(4000000)
    
    while n == 0:
        n = abs(n)
        print(lpd(primos, n))
        n = int(input())

    print()
main()
