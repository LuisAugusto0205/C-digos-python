def main():
    p, m, n = [int(x) for x in input().split()]
    while p > 0:
        saque = [tuple([int(x) if not i else x for i, x in enumerate(input().split())]) for _ in range(n)]
        maos = []

        for j in range(p):
            maos.append(saque[:m])
            saque = saque[m:]

        print(simulador(saque, maos, m, p) + 1)

        p, m, n = [int(x) for x in input().split()]
    
def simulador(saque, maos, m, p):
    topo = saque[0]
    saque = saque[1:]

    #varíaveis de status
    pula_vez = False
    compra = 0
    sentido = 1 # (1)horário, (-1)anti-horário
    
    j = 0#mao atual
    mudou = True#mudou o topo
    if mudou:
        sentido, compra, pula_vez = status(topo, sentido)
        mudou = False

    #imprime(maos, saque, topo)
    
    while True:                         
        j %= p #garante que existe o elemento j
        
        # procurando vencedor
        for i in range(len(maos)):
            if not maos[i]:
                return i
            
        # fase compra
        compra = comprar(compra, maos[j], saque)
        
        # fase descarte
        if not pula_vez:
            topo, mudou = descarte(topo, maos[j], saque)
        pula_vez = False

        #imprime(maos, saque, topo)
        
        #atualiza status
        if mudou:
            sentido, compra, pula_vez = status(topo, sentido)
            mudou = False
            
        #próximo jogador
        j += sentido

def imprime(maos, saque, topo):
    print('#'*40)
    for i in range(len(maos)):
        print('jogador {}: {}'.format(i+1, ' '.join([str(x) for x in maos[i]])))
    print('Topo: {}'.format(topo))
    print('saque: {}'.format(saque))

def descarte(topo, mao, saque):
    ''' realiza uma jogada e retorna o novo topo da pilha de descarte
        e se ele foi alterado'''
    valor_naipe = { 'C': 0.1, 'D': 0.2, 'H': 0.3, 'S': 0.4}
    naipe = topo[1]
    valor = topo[0]
    descartaveis = []
    
    for i in range(len(mao)):
        if mao[i][0] == valor or mao[i][1] == naipe:
            descartaveis.append(mao[i] + tuple([i]))
            
    if descartaveis:#escolhe carta com valor mais alto e a descarta
        m_carta = descartaveis[0]
        
        for carta in descartaveis:
            if carta[0] + valor_naipe[carta[1]] > m_carta[0] + valor_naipe[m_carta[1]]:
                m_carta = carta
                
        del mao[m_carta[2]]
        return m_carta[:2], True

    #caso o jogador não possua cartas validas em sua mão,
    #ele compra 1 carta e tenta descarta-la,
    #em caso de falha a carta é adicionada a sua mão.
    comprar(1, mao, saque)
    
    if mao[-1][0] == topo[0] or mao[-1][1] == topo[1]:
        topo = mao[-1]
        del mao[-1]
        return topo, True

    return topo, False

def status(topo, sentido):
    ''' verifica cartas especiais 1, 7, 11, 12'''
    compra = 0
    pula_vez = False
    
    if topo[0] == 12:
        sentido = -1 * sentido
        
    elif topo[0] == 7 or topo[0] == 1 or topo[0] == 11:
        compra = 1*(topo[0] != 11) + (topo[0] == 7)
        pula_vez = True

    return sentido, compra, pula_vez

def comprar(compra, mao, saque):
    '''comprar 1 ou 2 carta do baralho'''
    for _ in range(compra):
        if not saque:
            break
        mao.append(saque[0])
        del saque[0]
            
    return 0
main()
