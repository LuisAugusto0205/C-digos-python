import heapq
acr = [(0, 1), (-1, 0),
       (0, -1), (1, 0)]# acresimos

def main():
    n = int(input())
    passou = [[False]*110 for _ in range(110)]
    dista = [[10001]*110 for _ in range(110)]
    mina = []
    
    for _ in range(n):
        mina.append([int(x) for x in input().split()])

    d = Dijkstra(0, 0, mina, n, passou, dista)

    print(dista[n-1][n-1])

def Dijkstra(x, y, mina, n, passou, dista):
    global acr
    
    dista[x][y] = 0
    heap = []
    heapq.heappush(heap, (dista[x][y], (x, y)))

    while True:
        x = y = -1
        while len(heap) > 0:
            if not passou[x][y]:
                d, cd = heapq.heappop(heap)
                x, y = cd
                break

        if x == -1: break

        passou[x][y] = True
        
        for acr_x, acr_y in acr:
            if 0 <= x + acr_x < n and 0 <= y + acr_y < n:
                if dista[x + acr_x][y + acr_y] > dista[x][y] + mina[x + acr_x][y + acr_y]:
                    dista[x + acr_x][y + acr_y] = dista[x][y] + mina[x + acr_x][y + acr_y]

                if not passou[x + acr_x][y + acr_y]:
                    passou[x + acr_x][y + acr_y] = True
                    heapq.heappush(heap, (dista[x + acr_x][y + acr_y], (x + acr_x, y + acr_y)))

main()    
