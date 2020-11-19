def main():
    n = int(input())
    botas = []
    for _ in range(n):
        bota = input().split()
        botas.append((int(bota[0]), bota[1]))

    botas.sort(key = comparacao)

    print(solve(botas))

def solve(botas):
    pares = 0
    while len(botas) > 0:
        i = bbin(botas[1:], botas[0])
        if i == -1:
            botas = botas[1:]
        else:
            botas = botas[1:i+1] + botas[i+2:]
            pares += 1
    return pares

def comparacao(bota):
    if bota[1] == 'D':
        return bota[0] + 0.3
    else:
        return bota[0] + 0.5

def bbin(botas, bota):
    s = len(botas) - 1
    i = 0

    while s >= i:
        meio = (s + i)//2
        if bota[0] == botas[meio][0]:
            if bota[1] != botas[meio][1]:
                return meio
            elif botas[meio][1] == 'D':
                i = meio + 1
            else:
                s = meio - 1
        elif botas[meio][0] > bota[0]:
            s = meio - 1
        else:
            i = meio + 1
    return -1

main()
