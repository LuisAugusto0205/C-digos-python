def main():
    t = int(input())
    for _ in range(t):
        comeco = int(input())
        n, m = [int(x) for x in input().split()]
        grafo = [[] for _ in range(n)]
        passou = [False for _ in range(n)]
        
        for _ in range(m):
            u, v = [int(x) for x in input().split()]
            grafo[u].append(v)
            grafo[v].append(u)

        qnt = DFS(comeco, grafo, passou, 1)#quantidade de pontos ligados

        print((qnt - 1)*2)
         
def DFS(u, grafo, passou, qnt = 1):
    passou[u] = True
    tem_vizinho = False
    
    for v in grafo[u]:
        if not passou[v]:
            tem_vizinho = True
            qnt += DFS(v, grafo, passou, 1)

    if not tem_vizinho:
        return 1
    return qnt

main()
