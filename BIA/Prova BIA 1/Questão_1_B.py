def main():
    produto = input('Nome do produto: ')
    numero_ingredientes = int(validar_numero('Quantidade de ingredientes diferentes: ', []))
    custo = 0
    
    for i in range(numero_ingredientes):
        custo += calcular_custo_ingrediente(produto, i)

    custo *= 1.15

    print('Para fazer {} custa R${:<.2f} Reais'.format(produto, custo))

def calcular_custo_ingrediente(produto, i):    
    nome = input('\nQual o nome do {}º ingradiente? '.format(i + 1))
    print('\nExemplos de medidas: unidade, ml, gramas...')
    medida_receita = input('Como é medido o ingrediente {}? '.format(nome))

    pergunta = 'Quanto em {} de {} é usado na receita? '
    quantidade_receita = validar_numero(pergunta, [medida_receita, nome])

    if input('\nNo mercado é utilizada essa mesma medida?(s/n)') == 's':
        pergunta = 'Qual a quantidade em {} padrão que o mercado vende {}? '
        quantidade_vendida = validar_numero(pergunta, [medida_receita, nome])
        
        pergunta = 'Quanto custa {} {} de {} no mercado? '
        valor_mercado = validar_numero(pergunta, [quantidade_vendida, medida_receita, nome])

        
        custo = (quantidade_receita/quantidade_vendida) * valor_mercado

    else:
        pergunta = 'Qual a medida utilizada no mercado para comercializar {}? '
        medida_mercado = input(pergunta.format(nome))

        pergunta = 'Qual a quantidade em {} padrão que o mercado vende {}? '
        quantidade_vendida = validar_numero(pergunta, [medida_mercado, nome])

        pergunta = 'Quanto vale 1 {} em {}? '
        proporcao = validar_numero(pergunta, [medida_receita, medida_mercado])
        
        pergunta = 'Quanto custa {} {} de {} no mercado? '
        valor_mercado = validar_numero(pergunta, [quantidade_vendida, medida_mercado, nome])

        quantidade_receita_medida_mercado = proporcao * quantidade_receita

        custo = (quantidade_receita_medida_mercado/quantidade_vendida) * valor_mercado

    print()
    
    return custo

def validar_numero(pergunta, lista_variaveis):
    erro = True
    while erro:
        try:
            numero = float(input(pergunta.format(*lista_variaveis)))
            erro = False
        except:
            print('informe um valor!')
            erro =  True

    return float(numero)

if __name__ == '__main__':
    main()
