def crivo(n):
    primos = [True] * n
    primos[0] = primos[1] = False

    for i in range(4, n, 2):
        primos[i] = False

    i = 3
    while i * i <= n:
        if primos[i]:
            for j in range(i * i, n, i):
                primos[j] = False
        i += 2

    return primos

print(crivo(20))
    
        
