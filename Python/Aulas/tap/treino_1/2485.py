from queue import Queue
ax = [0, 1, 0, -1, 1, -1, 1, -1]
ay = [1, 0, -1, 0, 1, 1, -1, -1]

def main():
    global ax, ay
    t = int(input())
    
    for _ in range(t):
        l, c = [int(x) for x in input().split()]
        mapa = []
        
        for k in range(l):
            mapa.append([int(x) for x in input().split()])
            
        for i in range(l):
            for j in range(c):
                qnt = 0
                for w in range(8):
                    if 0 <= i + ax[w] < l and 0 <= j + ay[w] < c and mapa[i + ax[w]][j + ay[w]] == 1:
                        qnt += 1

        x, y = [int(x) - 1 for x in input().split()]

        print(BFS(x, y, mapa, l, c) - 1)

def BFS(x, y, matriz, l, c):
    global ax, ay
    
    resposta = 0
    fila = Queue()
    
    if matriz[x][y] == 1:
        fila.put((2, x, y))
        matriz[x][y] = 2

    while not fila.empty():
        dia, x, y = fila.get()
            
        for i in range(8):
            if 0 <= x + ax[i] < l and 0 <= y + ay[i] < c and matriz[x + ax[i]][y + ay[i]] == 1:
                matriz[x + ax[i]][y + ay[i]] = dia + 1
                fila.put((dia + 1, x + ax[i], y + ay[i]))

        if fila.empty():
            resposta = dia - 1  
    
    return resposta

main()
