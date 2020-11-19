def main():
    n = int(input())
    matriz = [[int(x) for x in input().split()] for _ in range(n)]
    resposta = []
    
    for linha in matriz:
        elem = linha[0]
        for i in range(1, len(linha)):
            elem = mdc(elem, linha[i])
        resposta.append(elem)

    print(' '.join([str(x) for x in resposta]))
    
def mdc(a, b):
    if a == 0: return b
    if b == 0: return a

    while a % b != 0:
        a, b = b, a%b

    return b

main()
