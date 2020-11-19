from queue import PriorityQueue, Queue

def main():
    n, c, f, m = [int(x) for x in input().split()]
    grafo = [[] for _ in range(505)]
    passou = [False] * 505
    dist = [10000] * 505

    for _ in range(m):
        u, v, t = [int(x) for x in input().split()]

        grafo[u].append((t, v))

    Dijkstra(c, grafo, passou, dist)

    if dist[f] < 10000:
        print(dist[f])
    else:
        print('*')

def Dijkstra(u, grafo, passou, dist):
    heap = PriorityQueue()
    heap.put((1, u))
    dist[u] = 0

    while not heap.empty():
        u = heap.get()[1]
        if passou[u]: continue

        passou[u] = True

        for t, v in grafo[u]:
            if dist[v] > dist[u] + 1:
                if (t == 1 and dist[u]%3 == 0) or (t == 0 and dist[u]%3 > 0):
                    dist[v] = dist[u] + 1
                    heap.put((dist[v], u))

