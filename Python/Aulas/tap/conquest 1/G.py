from queue import PriorityQueue

def main():
    k = int(input())

    for _ in range(k):
        n, m, s, t = [int(x) for x in input().split()]

        grafo = [[] for _ in range(20000)]
        passou = [False]*20000
        dist = [10000000]*20000

        for _ in range(m):
            u, v, w = [int(x) for x in input().split()]

            grafo[u].append((w, v))
            grafo[v].append((w, u))

        Dijkistra(s, grafo, passou, dist)

        print('Case #{}: '.format(k + 1), end = '')
        if dist[t] == 10000000:
            print('unreachable')
        else:
            print(dist[t])


def Dijkistra(fonte, grafo, passou, dist):
    filap = PriorityQueue()
    filap.put((0, fonte))
    dist[fonte] = 0

    while not filap.empty():
        u = filap.get()[1]

        if passou[u] == True: continue

        passou[u] = True

        for w, v in grafo[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                filap.put((dist[v], v))


main()
