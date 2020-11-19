def main():
    c, l = [int(x) for x in input().split()]
    matriz = [[10000000 for i in range(c)] for j in range(c)] #matriz de adjacência

    for _ in range(l):
        u, v, p = [int(x) for x in input().split()]

        if p < matriz[u][v]:
            matriz[u][v] = p
            matriz[v][u] = p

    Froyd_warshall(matriz, c)

    resposta = None
    for u in range(c):
        davez = max(matriz[u]) #pega a cidade mais distante da cidade 'u'
        if resposta is None or davez < resposta:
            resposta = davez

    print(resposta)

def Froyd_warshall(matriz, n):
    '''devolve a distancia de cada cidade para todas as outras'''
    for k in range(n):
        matriz[k][k] = 0
        for i in range(n):
            for j in range(n):
                if matriz[i][k] + matriz[k][j] < matriz[i][j]:
                     matriz[i][j] = matriz[i][k] + matriz[k][j]
main()
