def main():
    n = int(input())
    pecas = [[] for _ in range(100100)]

    #construção do grafo
    for _ in range(n):
        u, v = [int(x) for x in input().split()]
        pecas[v].append(u)
        #if v == 0: raiz = u

    resposta = DFS(0, pecas, [], 0)
    
    if resposta: print('bem')
    else: print('mal')
    
def DFS(v, pecas, sub, raiz):
    sub = []
    if not pecas[v]:
        return 1
    
    for u in pecas[v]:
        sub.append(DFS(u, pecas, sub[:], raiz))

    for i in range(len(sub)):
        if sub[0] != sub[i] or sub[i] == False:
            return False
        
    if raiz == v:
        return True
    return sub[0]*len(sub) + 1

main()
