from queue import Queue

def main():
    n = int(input())
    
    while n > 0:
        m = int(input())
        grafo = [[] for _ in range(200)]
        passou = [0]*200

        for _ in range(m):
            u, v = [int(x) for x in input().split()]

            grafo[u].append(v)
            grafo[v].append(u)

        if BFS(0, grafo, passou):
            print('BICOLORABLE')
        else:
            print('NOT BICOLORABLE')

        n = int(input())

def BFS(fonte, grafo, passou):

    fila = Queue()
    fila.put((1, fonte))

    while not fila.empty():
        c, u = fila.get()

        passou[u] = c

        for v in grafo[u]:
            if (passou[v] == c):
                return False
            elif passou[v] == 0:
                fila.put((2 if c == 1 else 1, v))
                passou[v] = 2 if c == 1 else 1

    return True

main()
