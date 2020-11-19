def main():
    #Dados de entrada
    n, k, m = [int(x) for x in input().split()]
    coef = [int(x) for x in input().split()]
    bases = [int(x) for x in input().split()]

    #Função recursiva (DP Botton-Up)
    def f(x):
        im = bases[:]
        for _ in range(n, x+1):
            im.append('')
        for j in range(n, x):
            s = 0
            for w in range(1, n+1):
                s += coef[w-1] *im[j-w]
            im[j] = s
        return im[x-1]
    
    #Saída
    print(f(k)%m)

main()
