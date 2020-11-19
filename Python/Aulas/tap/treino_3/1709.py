def main(p):
    #p = int(input())
    fim = [i for i in range(1, p + 1)]
    atual = fim[:]
    
    resp = 0
    while True:
        aux = []
        for i in range(p//2):
            aux.append(atual[i + p//2])
            aux.append(atual[i])

        resp += 1
        if aux == fim:
            break

        atual = aux

    print(resp)

def teste():
    for i in range(2, 101, 2):
        print('{} - '.format(i), end = '')
        main(i)
