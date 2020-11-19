def main():
    p, s = [int(x) for x in input().split()]
    cobertura = []
    
    for _ in range(s):
        cobertura.append(tuple([int(x) for x in
                            input().split()]))

    cobertura.sort(key = lambda t: t[1])

    i = 0
    while i < len(cobertura) - 1:
        if cobertura[i][0] > cobertura[i + 1][0] and cobertura[i][1] > cobertura[i + 1][1] and cobertura[i][0] <= cobertura[i + 1][1]:
            cobertura[i] = tuple([cobertura[i + 1][0], cobertura[i][1]])
            del cobertura[i + 1]
            continue
        
        elif cobertura[i][0] < cobertura[i + 1][0] and cobertura[i][1] < cobertura[i + 1][1] and cobertura[i][1] >= cobertura[i + 1][0]:
            cobertura[i] = tuple([cobertura[i][0], cobertura[i + 1][1]])
            del cobertura[i + 1]
            continue
        
        elif cobertura[i][0] >= cobertura[i + 1][0] and cobertura[i][1] <= cobertura[i + 1][1]:
            cobertura[i] = cobertura[i + 1]
            del cobertura[i + 1]
            continue
        
        elif cobertura[i][0] <= cobertura[i + 1][0] and cobertura[i][1] >= cobertura[i + 1][1]:
            del cobertura[i + 1]
            continue

        i += 1    
    
    #impressão dos dados
    for resposta in cobertura:
        print('{} {}'.format(*resposta))
    print()
main()
