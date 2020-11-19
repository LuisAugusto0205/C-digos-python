def multsort(renas, criterios):
    from operator import itemgetter
    #renas[i] = (nome, peso, idade, altura)
    #ordenação = 1, 2, 3, 0
    for i, reverso in reversed(criterios):
        renas.sort(key = itemgetter(i), reverse = reverso)

def main():
    criterios = ((1, True), (2, False), (3, False), (0, False))
    
    t = int(input())
    for i in range(t):
        n, m = [int(x) for x in input().split()]
        renas = []
        
        for _ in range(n):
            rena = input().split()
            renas.append((rena[0], int(rena[1]),
                          int(rena[2]), float(rena[3])))


        multsort(renas, criterios)

        print('CENARIO {' + str(i + 1) + '}')
        for k in range(m):
            print('{} - {}'.format(k + 1, renas[k][0]))

main()
                         
