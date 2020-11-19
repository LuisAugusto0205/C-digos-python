import os
def main():
    print('\nInsira a lista de palavras chaves, quando acabar apenas aperte enter!\n')
    
    chaves = []
    chave = input('Insira uma palavra chave: ')

    while chave:
        chaves.append(chave)
        chave = input('Insira mais uma palavra chave: ')

    caminho = input('\nInsira o caminho do arquivo: ')

    if os.path.isfile(caminho):
        with open(caminho, 'r+') as arquivo:
            novo_conteudo = []
            
            linha = arquivo.readline().rstrip('\n')
            while linha:
                novo_conteudo.append(filtrar_frase(chaves, linha))
                linha = arquivo.readline().rstrip('\n')

            arquivo.seek(0)
            arquivo.truncate()

            for linha in novo_conteudo:
                arquivo.write(linha)

    else:
        print('Caminho não encontrado!')
        

def filtrar_frase(chaves, frase):
    nova_frase = []
    for palavra in frase.split(' '):
        if palavra not in chaves:
            nova_frase.append(palavra)

    return ' '.join(nova_frase) + '\n'

if __name__ == '__main__':
    main()
