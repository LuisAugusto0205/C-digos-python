from queue import Queue

def main():
    t = int(input())
    grafo = [[] for _ in range(10001)]

    for i in range(0, 10001):
        grafo[i].append(i + 1)
        inv = inverso(i)
        if inv != i:
            grafo[i].append(inverso(i))

    
    for _ in range(t):
        processado = [False]*10000
        a, b = [int(x) for x in input().split()]
        
        if a != b:
            print(bfs(grafo, a, b, processado))
        else:
            print(0)

def bfs(grafo, a, b, processado):
    fila = Queue()
    fila.put((0, a))
    processado[a] = True
    achou = False

    while not fila.empty():
        p, u = fila.get()
        
        for v in grafo[u]:
            if v == b:
                return p + 1
            elif not processado[v]:
                fila.put((p + 1, v))
                processado[v] = True
        
def inverso(n):
    inv = tam = 0
    for lim in [10, 100, 1000, 10000]:
        if n >= lim: tam += 1
    
    while n > 0:
        inv += (n%10) * (10 ** tam)
        n //= 10
        tam -= 1

    return inv

main()
