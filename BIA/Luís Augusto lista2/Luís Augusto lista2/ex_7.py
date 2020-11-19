def main():
    n = ord('A')
    ordem = [[int(input('{}:'.format(chr(n + i)))),
              chr(n + i)] for i in range(4)]


    i = ordem.index(max(ordem))
    ordem[3], ordem[i] = ordem[i], ordem[3]

    i = ordem.index(min(ordem))
    ordem[0], ordem[i] = ordem[i], ordem[0]

    if ordem[1] > ordem[2]:
        ordem[1], ordem[2] = ordem[2], ordem[1]
    
    print(' '.join([lista[1] for lista in ordem]))

if __name__ == '__main__':
    main()
