from queue import Queue
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
def main():
    h, w = [int(x) for x in input().split()]
    grid = []

    for i in range(h):
        linha = []
        for j, char in enumerate(input()):
            linha.append(char)
            if char == '.':
                x = i
                y = j
        grid.append(linha)

    dic = {i:False for i in range(400)}
    resp = BFS(x, y, grid, h, w, [[False]*w for _ in range(h)], dic)

    print(resp + 1)
    
def BFS(x, y, grafo, h, w, passou, dic):

    fila = Queue()
    fila.put((0, x, y))
    max_rep = 0
    
    while not fila.empty():
        c, x, y = fila.get()

        for i in range(4):
            if 0 <= x + dx[i] < h and 0 <= y + dy[i] < w and grafo[x + dx[i]][y + dy[i]] == '.' and not passou[x + dx[i]][y + dy[i]]:
                fila.put((c + 1, x + dx[i], y + dy[i]))
                if dic[c]: max_rep = max(max_rep, c)
                dic[c] = True
                passou[x + dx[i]][y + dy[i]] = True
                
    return c + max_rep

main()
