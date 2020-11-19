from queue import Queue

def main():
    n, k = [int(x) for x in input().split()]
    grafo = [[] for _ in range(55)]
    
    for i in range(n):
        for j, num in enumerate(input().split()):
            if num == '1':
                grafo[i].append(j)

    resp = 0
    for i in range(n):
        resp += BFS(i, grafo, k, [False]*55, resp)

    print(resp)
    
def BFS(fonte, grafo, k, passou, resp):
    fila = Queue()
    fila.put(fonte)
    nivel = -1

    while not fila.empty():
        nivel += 1
        u = fila.get()

        for v in grafo[u]:
            if not passou[v]:
                fila.put(v)
                if nivel == k:
                    resp += 1
                passou[v] = True

    return resp
