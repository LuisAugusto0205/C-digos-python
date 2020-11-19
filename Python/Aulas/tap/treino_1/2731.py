from queue import PriorityQueue

def main():
    c, e = [int(x) for x in input().split()]
    while c > 0  and e > 0:
        grafo = [[] for _ in range(c)]
        rota = [-1] * c
        processou = [False] * c
        dist = [10000000] * c
        resposta = ''

        for _ in range(e):
            u, v, t = [int(x) for x in input().split()]
            u -= 1
            v -= 1

            grafo[u].append((t, v))
            grafo[v].append((t, u))

        d = int(input()) - 1

        Dijkistra(d, grafo, rota, processou, dist)

        tempo = dist[0]
        if tempo < 120:
            resposta += 'Will not be late. Travel time - {} - best way - '.format(tempo)
        else:
            resposta += 'It will be {} minutes late. Travel time - {} - best way - '.format(tempo - 120, tempo)

        x = 0
        caminho = []
        while rota[x] != x:
            caminho.append(str(x + 1))
            x = rota[x]
            if rota[x] == x:
                caminho.append(str(d + 1))
                resposta += ' '.join(caminho[::-1])

        print(resposta)
        
        c, e = [int(x) for x in input().split()]
    
def Dijkistra(u, grafo, rota, processou, dist):
    heap = PriorityQueue()
    heap.put((0, u))
    rota[u] = u
    dist[u] = 0
    
    while not heap.empty():
        p, u  = heap.get()
        if processou[u]: continue

        processou[u] = True

        for p, v in grafo[u]:
            if dist[v] > dist[u] + p:
                dist[v] = dist[u] + p
                heap.put((dist[v], v))
                rota[v] = u

main()
