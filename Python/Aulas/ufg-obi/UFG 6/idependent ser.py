from queue import Queue
from math import factorial as fat

def main():
    n = int(input())
    grafo = [[] for _ in range(n)]

    for _ in range(n - 1):
        u, v = [int(x) for x in input().split()]
        u -= 1
        v -= 1

        grafo[u].append(v)
        grafo[v].append(u)

    resp = 2
    num_preto = bfs(0, grafo, n) #primera forma de pintar arternadamente

    for i in range(1, num_preto + 1):
        resp += comb(num_preto, i)

    num_preto = n - num_preto

    for i in range(1, num_preto + 1):
        resp += comb(num_preto, i)

    print(resp - 1)
   
def comb(n, k):
    return fat(n)//(fat(k)*fat(n - k))

def bfs(fonte, grafo, n):
    cor = [-1]*n
    fila = Queue()
    cor[fonte] = 1 # 1 - Preto e 0 - Branco
    fila.put(fonte)
    
    while not fila.empty():
        u = fila.get()

        for v in grafo[u]:
            if cor[v] == -1:
                cor[v] = 1 - cor[u]
                fila.put(v)

    return sum(cor) #retorna o número de vertices pretos

main()
