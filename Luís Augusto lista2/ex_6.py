def main():
    n = int(input('tamanho da sequencia de fibonacci: '))
    fib = [0]*n
    fib[0] = fib[1] = 1

    for i in range(2, n):
        fib[i] += fib[i - 1] + fib[i - 2]

    print(' '.join([str(x) for x in fib]))

if __name__ == '__main__':
    main()

    
    
