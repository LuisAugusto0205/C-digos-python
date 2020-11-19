grafo = [[1, 3], [0, 2, 5],
         [1, 5, 3], [2, 0],
         [5], [1, 2, 4], [7],
         [6], []]

componentes = [-1 for _ in range(9)]

def main():
    global grafo, componentes
    componente = 0
    
    for v in range(9):
        if componentes[v] == -1:
            componente += 1
            componentes[v] = componente
            DFS(v)

    print(componente)
    
def DFS(v):
    global grafo, componentes

    for u in grafo[v]:
        if componentes[u] == -1:
            componentes[u] = componentes[v]
            DFS(u)
            
