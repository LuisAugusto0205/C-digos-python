from queue import PriorityQueue

def main():
    inf = 9999999
    n, m = [int(x) for x in input().split()]
    grafo = [[] for _ in range(n)]
    dist = [inf]*n
    processado = [False]*n
    
    for _ in range(m):
        u, v, p = [int(x) for x in input().split()]

        grafo[u].append((p, v))
        grafo[v].append((p, u))

    print(Prim(0, grafo, dist, processado))


def Prim(fonte, grafo, dist, processado):
    dist[fonte] = 0
    heap = PriorityQueue()
    heap.put((0, fonte))

    while not heap.empty():
        u = heap.get()[1]

        if processado[u]: continue

        processado[u] = True

        for p, v in grafo[u]:
            if not processado[v] and dist[v] > p:
                dist[v] = p
                heap.put((dist[v], v))

    return sum(dist)
