import heapq

passou = [False] * 10010
distancia = [99999] * 10010

def main():
    v, a = [int(x) for x in input().split()]
    fonte = int(input())
    lista_adjacencia = [[] for _ in range(v + 1)]

    #constroi grafos
    for _ in range(a):
        u, v, p = [int(x) for x in input().split()]

        lista_adjacencia[u].append((p, v))
        lista_adjacencia[v].append((p, u))

    print(Dijkstra(fonte, lista_adjacencia))
    passou = [False] * 10010
    distancia = [99999] * 10010
    
def Dijkstra(fonte, lista_adjacencia):
    global passou, distancia

    distancia[fonte] = 0
    heap = []
    heapq.heappush(heap, (0, fonte))

    while True:
        u = -1
        while len(heap) > 0:
            tupla = heapq.heappop(heap)
            if not passou[u]:
                u = tupla[0]
                break
            
        if u == -1:
            break
        
        passou[u] = True
        
        for d, v in lista_adjacencia[u]:
            if distancia[v] > distancia[u] + d:
                distancia[v] = distancia[u] + d
                heapq.heappush(heap, (distancia[v], v))

    return distancia[:8]    
        

        
