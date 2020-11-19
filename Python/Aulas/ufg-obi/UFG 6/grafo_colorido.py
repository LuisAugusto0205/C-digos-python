def main():
    n = int(input())
    raiz = None
    grafo = [[] for _ in range(n)]

    for _ in range(n - 1):
        u, v = [int(x) for x in input().split()]
        u -= 1
        v -= 1
        
        if raiz is None or raiz == v:
            raiz = u

        grafo[u].append(v)

    resp = dfs(raiz, grafo, 1) + dfs(raiz, grafo, 0)
    print(resp)
        
def dfs(u, grafo, corPai):
    pos = 0
    if len(grafo[u]) == 0:
        return 1
    
    for v in grafo[u]:
        if corPai:
            pos += dfs(v, grafo, 1) + dfs(v, grafo, 0)
        else:
            pos += dfs(v, grafo, 1)

    return pos
