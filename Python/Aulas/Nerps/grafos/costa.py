def main():
    try:
        m, n = [int(x) for x in input().split()]
    except:
        m, n = [int(x) for x in input().split()]
    
    areas = [[False] for _ in range((m + 2)*(n + 2))]
    
    for w in range(m):
        linha = '.' + input() + '.'
        for j, char in enumerate(linha[1: n + 1]):
            pos = w*(n + 2) + j
            areas[pos][0] = (char == '#')
            areas[pos].append(pos + 1)
            areas[pos].append(pos - 1)
            areas[pos].append(pos + (n + 2))
            areas[pos].append(pos - (n + 2))
     
    print(costas(areas))

def costas(areas):
    contador = 0
    
    for i in range(len(areas)):
        if areas[i][0] == True:
            for j in areas[i][1:]:
                if areas[j][0] == False:
                    contador += 1
                    break

    return contador

main()
