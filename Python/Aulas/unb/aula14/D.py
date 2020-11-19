def main():
    n = int(input())
    segmentos = [tuple([int(x) for x in input().split()]) for _ in range(n)]
    minimo_inicio, indice = Min(segmentos, n)
    if max(segmentos, key = lambda tupla: tupla[1])[1] == minimo_inicio[1]:
        print(indice + 1)
    else:
        print(-1)

def Min(segmentos, n):
    minimo = segmentos[0]
    i = 0
    for j in range(n):
        if segmentos[j][0] < minimo[0]:
            minimo = segmentos[j]
            i = j
        elif segmentos[j][0] == minimo[0]:
            if segmentos[j][1] > minimo[1]:
                minimo = segmentos[j]
                i = j
    return minimo, i

main()
