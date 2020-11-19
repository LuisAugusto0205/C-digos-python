def main():
    n, m, l = [int(x) for x in input().split()]
    matriz = [[10000000]*n for _ in range(n)]

    for _ in range(m):
        a, b, c = [int(x) for x in input().split()]
        a -= 1
        b -= 1

        if c <= l:
            matriz[a][b] = matriz[b][a] = c
        else:
            matriz[a][b] = matriz[b][a] = -1

    fw(matriz)
    q = int(input())
    
    for _ in range(q):
        s, t = [int(x) for x in input().split()]
        s -= 1
        t -= 1
        if matriz[s][t] < 0 or matriz[s][t] == 10000000:
            print(-1)
        else:
            n = matriz[s][t]//l
            resp = n + 1*(matriz[s][t]%l and n > 1)
            print(resp)
    
def fw(matriz):
    for k in range(len(matriz)):
        matriz[k][k] = 0
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                if matriz[i][k] > 0 and matriz[k][j] > 0:
                    if matriz[i][j] > matriz[i][k] + matriz[k][j]:
                        matriz[i][j] = matriz[i][k] + matriz[k][j]

main()
