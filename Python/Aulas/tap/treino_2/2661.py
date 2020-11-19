from math import factorial

def crivo(n):
    numeros = [True]*(n + 1)
    numeros[0] = numeros[1] = False
    primos = []
    
    for i in range(4, n, 2):
        numeros[i] = False

    i = 3
    while i * i <= n:
        if numeros[i]:
            for j in range(i * i, n, i):
                numeros[j] = False
        i += 2

    for i in range(n + 1):
        if numeros[i]:
            primos.append(i)

    return primos

def fatores(n):
    primos = crivo(int(round(n ** 0.5 + 0.5, 0)))
    fat = []
    p = 2
    i = 0
    
    while p * p <= n:
        while n % p == 0:
            n //= p
            if len(fat) == 0 or fat[-1] != p: fat.append(p)
        
        i += 1
        p = primos[i]
        
    if n > 1: fat.append(n)

    return fat

def comb(n, k):
    return factorial(n)//(factorial(k)*factorial(n-k))

def main():
    n = int(input())
    x = len(fatores(n))
    resp = 0
    
    for k in range(2, x + 1):
        resp += comb(x, k)

    print(resp)

main()
