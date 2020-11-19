def main():
    a, v = [int(x) for x in input().split()]
    t = 0
    while a and v:
        t += 1
        aeroportos = [x for x in range(a)]
        voos = [[x] for x in range(a)]
        resposta = []
        
        for _ in range(v):
            u, v = [int(x) for x in input().split()]
            u -= 1
            v -= 1
            voos[u].append(v)
            voos[v].append(u)

        voos.sort(key = lambda lista: len(lista), reverse = True)

        tam = len(voos[0])
        resposta.append(voos[0][0] + 1)
        for i in range(1, len(voos)):
            if len(voos[i]) == tam:
                resposta.append(voos[i][0] + 1)

        resposta.sort()

        print('Teste {}'.format(t))
        for j in range(len(resposta)):
            if j == len(resposta) - 1: print(resposta[j])
            else: print(resposta[j], end = ' ')
        print()
        
        a, v = [int(x) for x in input().split()]
