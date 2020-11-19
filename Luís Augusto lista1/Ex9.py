def main():
    a = int(input('A: '))
    b = int(input('B: '))
    c = int(input('C: '))

    print('quandrado da soma é {}'.format((a+b+c) ** 2))
    print('quadrado do maior valor é {}'.format(max(a, b, c) ** 2))

main()
