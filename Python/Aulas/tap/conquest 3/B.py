def crivo(n):
    primos = [True] * n
    primos[0] = primos[1] = False

    i = 2
    while i * i < n:
        if primos[i] == True:
            for j in range(2*i, n, i):
                primos[j] = False
        i += 1
    return primos

def main():
    primos = crivo(100004)
    x = int(input())
    for i in range(x, 100004):
        if primos[i]:
            print(i)
            break

main()
    
            
