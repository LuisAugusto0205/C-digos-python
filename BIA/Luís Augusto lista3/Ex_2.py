def main():
    valores = [0]
    print('aperte apenas enter para finalizar!')
    novo_valor = input('Insira um novo valor: ')

    while novo_valor:
        valores.append(valores[-1] + int(novo_valor))
        media = valores[-1]/(len(valores) - 1)
        print('A media é {:.2f}'.format(media))
        novo_valor = input('Insira um novo valor: ')

if __name__ == '__main__':
    main()
        
