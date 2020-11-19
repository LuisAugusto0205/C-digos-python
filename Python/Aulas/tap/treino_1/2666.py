import sys
sys.setrecursionlimit(100000)
n, c = [int(x) for x in input().split()]
ouro = [int(x) for x in input().split()]
grafo = [[] for _ in range(n)]
passou = [False] * n

def main():
    global n, grafo, passou
    
    for _ in range(n - 1):
        u, v, k = [int(x) for x in input().split()]
        u -= 1
        v -= 1
        
        grafo[u].append((k, v))
        grafo[v].append((k, u))

    print(DFS(0, 0, 0))

def DFS(u, a, km):
    global n, c, grafo, ouro, passou
    passou[u] = True
    peso = 0
    
    for p, v in grafo[u]:
        if not passou[v]:
            peso += DFS(v, u, p)

    visitar = ouro[u]//c + (ouro[u]%c != 0)
    ouro[a] += ouro[u]
    ouro[u] = 0
    peso += 2*visitar*km
        
    
    return peso

main()            
