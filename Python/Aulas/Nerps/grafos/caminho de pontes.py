import heapq

def main():
    s, p = [int(x) for x in input().split()]
    pontes = [[] for _ in range(1010)]
    passou = [False] * 1010
    buracos = [None] * 1010

    for _ in range(p):
        try:
            s1, s2, b = [int(x) for x in input().split()]
            pontes[s1].append((b, s2))
            pontes[s2].append((b, s1))
        except EOFError:
            break

    dijkstra(0, pontes, passou, buracos)

    print(buracos[s + 1])
    
def dijkstra(fonte, pontes, passou, buracos):
    heap = []
    buracos[fonte] = 0
    heapq.heappush(heap, (buracos[fonte], fonte))
    
    while True:
        u = -1
        while len(heap) > 0:
            tupla = heapq.heappop(heap)
            if not passou[u]:
                u = tupla[1]
                break
        
        if u == -1: break        
        passou[u] = True    
        
        for bv, v in pontes[u]:
            if buracos[v] is None or buracos[v] > buracos[u] + bv:
                buracos[v] = buracos[u] + bv
                heapq.heappush(heap, (buracos[v], v))

main()
    
