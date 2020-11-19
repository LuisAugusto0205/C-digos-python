def main():
    n = int(input())
    for _ in range(n):
        painel = 0
        lampadas, k = [int(x) if x.isdigit() else x
                       for x in input().split()]
        t = len(lampadas)
        
        for i in range(t):
            if lampadas[i] == 'O':
                painel |= (1 << i)

        for i in range(k):
            painel = ~painel
            painel = abs(painel)
        
        for i in range(t):
            if painel & (1 << i):
                print('O', end = '')
            else:
                print('X', end =  '')

        print()

main()
        
