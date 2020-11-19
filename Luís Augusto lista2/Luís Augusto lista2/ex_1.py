def main():
    temperatura = float(input('Qual a temperatura da Caldeira?\n'))
    if temperatura > 300:
        print('Desligar')
    else:
        print('ligar')

if __name__ == '__main__':
    main()
