from random import randint, sample
direcao = ['Horizontal', 'Vertical']

def main():
    try:
        with open('Palavras_aleatorias_Questão_3.txt', 'r') as file:
            palavras = [palavra.upper() for palavra in file.readline().split(';')]
    except:
        print('Tente descopactar ou verificar se o arquivo Palavras_aleatorias_Questão_3.txt esta nessa pasta!')
        raise Exception('ERRO ao ler o arquivo Palavras_aleatorias_Questão_3.txt')

    print("minimo e máximo de linhas e colunas é 15 e 20 respectivamente!")
    linhas = int(input("número de linhas do caça palavras: "))
    colunas = int(input("número de colunas do caça palavras: "))
    
    linhas = max(min(20, linhas), 15)
    colunas = max(min(20, colunas), 15)

    matriz = gera_caca_palavras(linhas, colunas)
    matriz_resposta = [['*']*colunas for _ in range(linhas)]


    palavras_escolhidas = {}
    for palavra in sample(palavras, 8):
        posicao = gera_posicao(palavra, linhas, colunas, matriz_resposta)
        palavras_escolhidas[palavra] = posicao

    colocar_palavras(matriz, palavras_escolhidas)

    print('O novo caça palavras está pronto!\n')
    for i in range(linhas):
        linha = ' '.join(matriz[i])
        print(linha)
    print()

    if input('gerar resposta? (s/n)') == 's':
        print()
        colocar_palavras(matriz_resposta, palavras_escolhidas)
        for i in range(linhas):
            linha = ' '.join(matriz_resposta[i])
            print(linha)
        print()
        
        for i, palavra in enumerate(palavras_escolhidas.keys()):
            print('[{}] {}'.format(i + 1, palavra))
        
        
def colocar_palavras(matriz, palavras_escolhidas):
    for palavra, pos in palavras_escolhidas.items():
        direcao = pos[2]
        x = pos[0]
        y = pos[1]
        
        if direcao == 'Horizontal':
            for i, letra in enumerate(palavra):
                matriz[x][y + i] = letra.upper()

        elif direcao == 'Vertical':
            for i, letra in enumerate(palavra):
                matriz[x + i][y] = letra.upper()
    

def gera_caca_palavras(linhas, colunas):
    matriz = [['A']*colunas for i in range(linhas)]
    for i in range(linhas):
        for j in range(colunas):
            matriz[i][j] = chr(randint(ord('A'), ord('Z')))
            
    return matriz
    
def gera_posicao(palavra, linhas, colunas, matriz_resposta):
    deu_sobreposicao = True
    
    while deu_sobreposicao:
        d = randint(0, 1)
        
        if direcao[d] == "Horizontal":
            x = randint(0, linhas - 1)
            y = randint(0, colunas - len(palavra))
        elif direcao[d] == "Vertical":
            x = randint(0, linhas - len(palavra))
            y = randint(0, colunas - 1)

        #evitar sobreposição de palavras
        if direcao[d] == "Horizontal":
            local = [matriz_resposta[x][i] for i in range(y, y + len(palavra))]
            deu_sobreposicao = '1' in local
            if not deu_sobreposicao:
                for i in range(y, y + len(palavra)):
                    matriz_resposta[x][i] = '1'
                    
        elif direcao[d] == "Vertical":
            local = [matriz_resposta[i][y] for i in range(x, x + len(palavra))]
            deu_sobreposicao = '1' in local
            if not deu_sobreposicao:
                for i in range(x, x + len(palavra)):
                    matriz_resposta[i][y] = '1'
    

    return (x, y, direcao[d])

if __name__ == '__main__':
    main()
