IMC= ['IMC', 'abaixo de 18,5', 'entre 18,6 e 24,9', 'entre 25 e 29,9',
      'entre 30 e 34,9', 'entre 35 e 39,9', 'acima de 40']

classificacao = ['Classificação', 'abaixo do peso', 'Peso ideal', 'Levemente acima do peso',
                 'Obesidade grau I', 'Obesidade grau II (severa)', 'Obesidade grau III(mórbida)']

def main():
    tabela()
    IMC = float(input('Seu peso: '))/(float(input('Sua Altura: '))**2)
    marcador = classificar(IMC)

    tabela(marcador)
    print('Sua classificação está destacada na tabela!')
    
def tabela(marcar = -1):
    global IMC, classificacao

    print('+' + '-'*25 + '+' + '-'*37 + '+')
    
    for i in range(7):
        if i == marcar:
            print('+' + '{:^25}'.format(IMC[i]) + '|' + '{:^37}'.format(classificacao[i]) + '+')
            print('+'*65)
        else:
            print('|' + '{:^25}'.format(IMC[i]) + '|' + '{:^37}'.format(classificacao[i]) + '|')
            if i == marcar - 1:
                print('+'*65)
            else:
                print('+' + '-'*25 + '+' + '-'*37 + '+')
    
def classificar(IMC):
    if IMC < 18.5:
        return 1
    elif IMC <= 24.9:
        return 2
    elif IMC <= 29.9:
        return 3
    elif IMC <= 34.9:
        return 4
    elif IMC <= 39.9:
        return 5
    else:
        return 6

if __name__== '__main__':
    main()
