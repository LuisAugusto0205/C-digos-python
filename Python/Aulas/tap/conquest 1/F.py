from queue import Queue
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def main():
    n, m = [int(x) for x in input().split()]
    grid = []
    x = y = 0
    
    for i in range(n):
        linha = []
        for j, char in enumerate(input()):
            if char == 'E':
                x = i
                y = j
            linha.append(char)
        grid.append(linha)

    print(BFS(x, y, grid, n, m))

def BFS(x, y, grafo, n, m):

    fila = Queue()
    fila.put((0, x, y))
    grafo[x][y] = 'T'
    dist = None
    resp = 0
    
    while not fila.empty():
        c, x, y = fila.get()
        if dist is not None and dist > c:
            return resp
            
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a < n and 0 <= b < m and grafo[a][b] != 'T':              
                fila.put((c + 1, a, b))
                
                if grafo[a][b] == 'S':
                    dist = c
        
                if not grafo[a][b].isalpha() and grafo[a][b] > '0' and (dist is None or c == dist):
                    resp += int(grafo[a][b])

                grafo[a][b] = 'T'
                
    return resp

main()
