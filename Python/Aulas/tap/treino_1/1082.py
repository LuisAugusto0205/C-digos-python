def main():
    n = int(input())
    
    for k in range(n):
        v, e = [int(x) for x in input().split()]
        grafo = [[] for _ in range(v)]
        passou = [False for _ in range(v)]
        dic = {i:chr(ord('a') + i) for i in range(v)}
        resposta = []
        
        for _ in range(e):
            x, y = [ord(x) - ord('a') for x in input().split()]

            grafo[x].append(y)
            grafo[y].append(x)

        for i in range(v):
            componente = []
            if not passou[i]:
                DFS(i, grafo, passou, componente, dic)
                resposta.append(','.join(sorted(componente)) + ',')

        resposta.sort()
        print('Case #{}:'.format(k + 1))
        for comp in resposta: print(comp)
        print('{} connected components'.format(len(resposta)))
        print()
        
def DFS(u, grafo, passou, componente, dic):
    passou[u] = True
    componente.append(dic[u])

    for v in grafo[u]:
        if not passou[v]:
            DFS(v, grafo, passou, componente, dic)

main()
