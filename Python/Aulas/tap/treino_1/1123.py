from queue import PriorityQueue

def main():
    n, m, c, k = [int(x) for x in input().split()]
    while n > 0:
        grafo = [[] for _ in range(255)]
        caminho = [-1 for _ in range(255)]
        custo = [10000000 for _ in range(255)]
        processado = [False for _ in range(255)]
        rota = [0 for _ in range(c - 1)]

        for _ in range(m):
            u, v, p = [int(x) for x in input().split()]
            u, v= min(u, v), max(u, v)

            if u < c - 1 and v <= c - 1 and u + 1 == v:
                rota[u] = p
                grafo[u].append([0, v])
                grafo[v].append([0, u])
            else:
                grafo[u].append([p, v])
                grafo[v].append([p, u])
                
        tam_rota = sum(rota)
        dist_rota = rota[:]
        
        for i in range(c - 1):
            rota[i] = tam_rota - (i != 0)*dist_rota[i - 1]
            
            for j in range(len(grafo[i])):
                u = grafo[i][j][1]

                if u != i + 1 and u != i - 1:
                    grafo[i][j][0] += rota[i]
                    
                    for z in range(len(grafo[u])):
                        if grafo[u][z][1] == i:
                            grafo[u][z][0] += rota[i]
     
            tam_rota = rota[i]

        dijkstra(k, grafo, caminho, custo, processado)

        print(custo[c-1])
        
        n, m, c, k = [int(x) for x in input().split()]
        
        

def dijkstra(fonte, grafo, caminho, custo, processado):
    custo[fonte] = 0
    filaP = PriorityQueue()
    filaP.put((0, fonte))
    
    while not filaP.empty():
        p, u = filaP.get()

        if processado[u]: continue

        processado[u] = True

        for w, v in grafo[u]:
            if custo[v] > custo[u] + w:
                custo[v] = custo[u] + w
                filaP.put((custo[v], v))
                caminho[v] = u

main()
