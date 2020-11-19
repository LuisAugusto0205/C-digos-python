def main():
    n = int(input('Até que número a sequencia vai? '))
    paridade = input('sua sequência é de números pares?(s/n) ') == 's'
    crescente = input('sua senquência é crescente?(s/n) ') == 's'

    sequencia(n, paridade, crescente)

def sequencia(n, par = True, crescente = True):
    if par and crescente:
        print([i for i in range(2, n + 1, 2)])
    elif par and not crescente:
        print(sorted([i for i in range(2, n + 1, 2)], reverse = True))
    elif not par and crescente:
        print([i for i in range(1, n + 1, 2)])
    else:
        print(sorted([i for i in range(1, n + 1, 2)], reverse = True))

if __name__ == '__main__':
    main()
