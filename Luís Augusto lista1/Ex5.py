def main():
    a = int(input('A: '))
    b = int(input('B: '))
    a, b = b, a
    print('A: {}, B: {}'.format(a, b))
main()
