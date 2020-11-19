from queue import PriorityQueue

def main():
    try:
        n, m = [int(x) for x in input().split()]
    except:
        n = 0

    while n > 0:
        grafo = [[] for i in range(n)]
        processado = [False]*n
        prob = [0]*n

        for i in range(m):
            u, v, p = [int(x) for x in input().split()]
            u -= 1
            v -= 1

            grafo[u].append((p/100, v))
            grafo[v].append((p/100, u))

        dijkstra(grafo, processado, prob)
        print('{:.6f} percent'.format(prob[n - 1]*100))
        
        try:
            n, m = [int(x) for x in input().split()]
        except:
            break

def dijkstra(grafo, processado, prob):
    fila = PriorityQueue()
    fila.put((-100, 0))
    prob[0] = 1

    while not fila.empty():
        u = fila.get()[1]
        

        if processado[u]: continue
        processado[u] = True

        for p, v in grafo[u]:
            if prob[u] * p > prob[v]:
                prob[v] = prob[u] * p
                fila.put((-prob[v], v))

main() 
