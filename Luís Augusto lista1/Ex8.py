status = ['subiu', 'desceu']
def main():
    i = 1
    while i > 0:
        dolar = int(input('Valor em dolar: '))
        cota1 = float(input('cotação: '))

        print('O valor em reais é {}'.format(dolar * cota1))

        if i > 1:
            variacao = abs(((cota1 * 100)/cota2) - 100)
            print('o dolar {} {:.2f}%'.format(status[cota1 < cota2],
                                              variacao))

        if input('realizar coverção novamente?(S/N) ') != 'S':
            i = 0
        else:
            i += 1

        cota2 = cota1
        print()

main()
