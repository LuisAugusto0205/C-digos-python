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
