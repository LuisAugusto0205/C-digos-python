def main():
    print('Se quiser fazer o procedimento no diretório atual e arquivo a ser copiado esta nele')
    print('apenas entre com o nome do arquivo já existente e o nome do novo arquivo\n') 
    antigo = input('caminho do arquivo a ser copiado: ')
    valido = True
    try:
        arquivo = open(antigo, 'r')
        conteudo = arquivo.readlines()
        arquivo.close()
    except:
        print('Caminho não encontrado'.format(antigo))
        valido = False

    if valido:
        novo = input('caminho do novo arquivo: ')
        
        with open(novo, 'w') as novo_arquivo:
            for linha in conteudo:
                novo_arquivo.write(linha)

        print('Cópia feita com sucesso!')

if __name__ == '__main__':
    main()
        
