from random import randint #função que gera o número aleatório

Exemplo = [2, 3, 30, 60]

def matrizAleatoria(linha, coluna, intervalInicial, intervalFinal):
    matriz = []

    #criação
    for i in range(linha):
        l = []#nova linha
        for j in range(coluna):
            l.append(randint(intervalInicial, intervalFinal))
        matriz.append(l)
        
    #Impressão (Opcional)(obs: use fonte monoespaçadas. Ex: Courier New)
    print(('+'+'-'*5)*coluna + '+')
    for i in range(linha):
        for j in range(coluna):
            print('|{:^5}'.format(matriz[i][j]), end = '')
        print('|')
        print(('+'+'-'*5)*coluna + '+')
    print()
    
    return matriz

print(matrizAleatoria(*Exemplo))
