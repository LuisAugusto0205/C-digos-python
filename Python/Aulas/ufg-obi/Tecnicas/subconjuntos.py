def Sub(mask, pos, soma):
    global mem
    if soma > n:
        return

    if soma > mem[0]:
        mem = (soma, mask)
        
    if pos >= m:
        return

    Sub(mask | (1 << pos), pos + 1, soma + faixas[pos])
    Sub(mask, pos+1, soma)

while True:
    try:
        faixas = [int(x) for x in input().split()]
        n, m, faixas = faixas[0], faixas[1], faixas[2:]
        mem = (0,0) #mémoria(soma, mask)
        Sub(0, 0, 0)
        for i in range(m):
            if mem[1] & (1 << i):
                print(faixas[i], end = ' ')
        print('sum:{}'.format(mem[0]))
    except:
        break
