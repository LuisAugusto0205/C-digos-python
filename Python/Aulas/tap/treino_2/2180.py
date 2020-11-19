def crivo(k, n):
    primos = [True] * n
    primos[0] = primos[1] = False
    lista_primos = [2]

    for i in range(4, n, 2):
        primos[i] = False

    i = 3
    while i * i <= n:
        if primos[i]:
            for j in range(i * i, n, i):
                primos[j] = False
        i += 2

    j = None
    for i in range(len(primos)):
        if primos[i]:
            lista_primos.append(i)
            if j is None and i >= k:
                j = len(lista_primos) - 1

    if j is None: j = len(lista_primos)
    
    return j, lista_primos

def main():
    k = int(input())
    j, primos = crivo(k, 60000)
    s = soma = 0
    
    for i in range(j, len(primos)):
        if s == 10: break
        soma += primos[i]
        s += 1

    num = 60000
    while s < 10:
        num += 1
        e_primo = True
        
        for p in primos:
            if num % p == 0:
                e_primo = False
                break
            
        if e_primo:
            s += 1
            soma += num

    horas = 6*(10**7) // soma
    dias = horas // 24
    
    print('{} km/h'.format(soma))
    print('{} h / {} d'.format(horas, dias))

main()
        
