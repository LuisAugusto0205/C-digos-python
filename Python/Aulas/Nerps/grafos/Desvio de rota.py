import heapq
import bisect

def main():
    n, m, c, k = [int(x) for x in input().split()]
    passou = [False]*260
    pedagio = [[10000000, []] for _ in range(260)]
    cidades = [[] for _ in range(260)]
    rota = [x for x in range(c)]
    for _ in range(m):
        u, v, p = [int(x) for x in input().split()]

        cidades[u].append((p, v))
        cidades[v].append((p, u))

    Dijkstra(k, pedagio, passou, cidades)
    print(pedagio[:4])
    aux_j = c - 1
    for cidade in pedagio[c-1][1]:
        j1 = bisect.bisect_right(rota, cidade)
        j2 = bisect.bisect_left(rota, cidade)
        
        if j1 != j2:
            if rota[j2] == 0: break
            aux_j = j2 #cidade em quem volta para rota
            break

    resposta = pedagio[aux_j][0]
    
    if aux_j == c-1:
        print(resposta)
        return
    
    for x in range(aux_j + 1, c):
        for c in cidades[x]:
            if c[1] == x - 1:
                resposta += c[0]

    print(resposta)
    
            
def Dijkstra(fonte, pedagio, passou, cidades):
    heap = []
    pedagio[fonte][0] = 0
    heapq.heappush(heap, (pedagio[fonte][0], fonte))

    while True:
        u = -1
        while len(heap) > 0:
            c = heapq.heappop(heap)[1]
            
            if not passou[c]:
                u = c
                break
        if u == -1: break
        
        passou[u] = False

        for pv, v in cidades[u]:
            if pedagio[v][0] > pedagio[u][0] + pv:
                pedagio[v][0] = pedagio[u][0] + pv
                heapq.heappush(heap, (pedagio[v][0], v))
                pedagio[v][1] = pedagio[u][1] + [u]
        
             
