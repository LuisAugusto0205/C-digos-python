def main():
    n = int(input())

    naturais = [True]*(12000000)
    naturais[0] = naturais[1] = 0
    primos = [] 
    #crivo
    for i in range(2, 12000000):
        if naturais[i]:
            primos.append(i)
            for j in range(2*i, n + 1, i):
                naturais[j] = False

    print(primos[n-1])
main()
