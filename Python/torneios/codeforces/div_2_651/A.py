
def busca(fila, s):
    sup = len(fila) - 1
    inf = 0
    while sup >= inf:
        meio = (sup + inf)//2
        if fila[meio][0] == s:
            return meio
        elif fila[meio][0] > s:
            sup = meio - 1
        else:
            inf = meio + 1
n = int(input())
fila = [(int(x), i) for i, x in enumerate(input().split())]
m = int(input())
sairam = [int(x) for x in input().split()]
fila.sort(key = lambda t: t[0])
for s in sairam:
    j = busca(fila, s)
    del fila[j]

fila.sort(key = lambda t: t[1])
for i in range(len(fila)):
    if i == n - 1: print(fila[i][0])
    else: print(fila[i][0], end = ' ')
