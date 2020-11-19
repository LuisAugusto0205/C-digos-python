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

def main():
    primos = crivo(20000000)
    tabela = [(None, 1)]
    tp = 0
    while True:
        try:
            s = int(input())
            if s > len(tabela) - 1:
                for i in range(tabela[-1][1] + 1, len(primos)):
                    if primos[i - 1] + 2 == primos[i]:
                        tp += 1
                        tabela.append(((primos[i - 1], primos[i]), i))
                        if tp == s:
                            print('({}, {})'.format(primos[i - 1],
                                                    primos[i]))
                            break
            else:
                print('({}, {})'.format(*tabela[s][0]))
        except EOFError:
            break

main()
