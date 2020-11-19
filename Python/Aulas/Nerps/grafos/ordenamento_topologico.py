from queue import PriorityQueue

def main():
    n, m = [int(x) for x in input().split()]
    grafo = [[] for _ in range(n)]
    grau = [0]*n
    heap = PriorityQueue()
    lista = []
    
    for _ in range(m):
        u, v = [int(x) for x in input().split()]
        grau[v] += 1
        grafo[u].append(v)

    for i in range(n):
        if grau[i] == 0: heap.put(i)

    while not heap.empty():
        davez = heap.get()
        lista.append(davez)

        for v in grafo[davez]:
            grau[v] -= 1
            if grau[v] == 0:
                heap.put(v)
        
    
    if len(lista) == n:
        for i in range(n): print(lista[i])
    else: print('*')

main()
            
            
