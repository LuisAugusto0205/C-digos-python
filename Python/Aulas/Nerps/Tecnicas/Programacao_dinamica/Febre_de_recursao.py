def main():
    #Dados de entrada
    n, k, m = [int(x) for x in input().split()]
    coef = [int(x) for x in input().split()]
    bases = [int(x) for x in input().split()]

    #Lista da memória
    mem = bases[:]
    for i in range(n, k + 1):
        mem.append('')

    #Função recursiva
    def f(x):
        s = 0
        if x <= n: return bases[x - 1]
        for i in range(1, n+1):
            if mem[x-i] != '':
                s += coef[i-1]*mem[x-i]
            else:
                s += coef[i-1]*f(x-i)
        mem[x] = s
        return mem[x]

    #Saída
    print(f(k)%m)
    print(mem)
main()
