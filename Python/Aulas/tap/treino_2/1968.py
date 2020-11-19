def crivo(a, n, k):
    tabela = [0]*(n + 1)
    kDivisores = []
    
    R = int(n ** 0.5)
    for i in range(1, R + 1):
        tabela[i * i] += 1
        
        for j in range(i*i + i, n + 1, i):
            tabela[j] += 2
            
        
    
    for i in range(a, n + 1):
        if tabela[i] == k:
            kDivisores.append(i)

    return kDivisores

def main():
    a, b, k = [int(x) for x in input().split()]

    lideres = len(crivo(a, b, k))

    resp = lideres ** (((b - a) + 1) - lideres)
    print(resp)

main()
