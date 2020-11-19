def main():
    n = int(input())
    matriz = [[int(x) for x in input().split()] for _ in range(n)]
    resposta = []

    for i in range(n):
        resposta.append(int(matriz[i][i] ** 0.5))

    print(' '.join([str(x) for x in resposta]))

main()
