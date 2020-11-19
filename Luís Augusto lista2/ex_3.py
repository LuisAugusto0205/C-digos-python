def main():
    for i in range(1, 10):
        for j in range(1, 10):
            print('{}x{}= {:2}|'.format(j, i, i*j), end = ' ')
        print()
        
    print('\nMultiplicação (x)\nDivsão(/)\nAdição(+)\nSubtração(-)\n')
    expressao = input('Digite a conta:(Ex: 4 x 3, 16 / 4, 13 + 7, 12 - 5)\n')

    num1, op, num2 = operation(expressao)

    if op == 'x':
        print('{} x {} = {}'.format(num1, num2, num1 * num2))
    elif op == '/':
        print('{} / {} = {:.5}'.format(num1, num2, num1 / num2))
    elif op == '+':
        print('{} + {} = {}'.format(num1, num2, num1 + num2))
    elif op == '-':
        print('{} - {} = {}'.format(num1, num2, num1 - num2))
    else:
        print('operador não reconhecido!')

def operation(expressao):
    expressao = expressao.strip()
    componentes = expressao.split()

    if len(componentes) == 1:
        for char in expressao:
            if not char.isalnum() or char == 'x':
                operador = char
                num1, num2 = [float(x) for x in expressao.split(char)]

    else:
        num1 = float(componentes[0])
        operador = componentes[1]
        num2 = float(componentes[2])

    return num1, operador, num2

if __name__ == '__main__':
    main()
