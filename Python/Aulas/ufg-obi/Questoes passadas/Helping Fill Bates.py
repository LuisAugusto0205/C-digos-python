import bisect # esta biblioteca realiza a busca binária
dic = {}#dicionário {chave = letra: valor = lista de posições que a letra aparece}
def main():
    global dic
    #ler dados de entrada
    fila = input()
    quantidade_buscas = int(input())
    buscas = [input() for _ in range(quantidade_buscas)]
    #chama as funções
    Constroi_Dicionario_Por_Letra(fila)
    Verifica_Cada_busca(buscas)
    
def Constroi_Dicionario_Por_Letra(fila):
    global dic
    for i in range(len(fila)):
        if fila[i] not in dic.keys(): #verifica se a letra já esta registrada no dicionário
            dic[fila[i]] = [i]
        else:
            dic[fila[i]] += [i]

def Verifica_Cada_busca(buscas):
    global dic
    for busca in buscas: #a iteração usa uma busca diferente da lista de buscas
        aux = -1 #variavel auxiliar para o indice de um letra dentro da fila
        indice = -1 #indice da letra procurada a cada iteração
        for j in range(len(busca)):# passa por todas os indices das letras de uma busca 
                try:
                    aux = bisect.bisect_right(dic[busca[j]], indice)#encontra o indice do primeiro elemento maior que indice da letra anterior
                    if aux == len(dic[busca[j]]): # se o auxiliar for igual ao tamanho da lista de aparicoes da letra procurada, então não foi encontrado
                        print('Not matched')
                        break
                    else:
                        indice = dic[busca[j]][aux] # retorna o índice da letra procurada
                    if j == 0:#Para mostrar a saída
                        primeiro_indice = indice
                    if j == len(busca) - 1:
                        ultimo_indice = indice
                        print('Matched {} {}'.format(primeiro_indice, ultimo_indice))
                except KeyError: # entra aqui caso a letra procurada não exista nas letras registradas no dicionario
                    print('Not matched')
                    break

main()
