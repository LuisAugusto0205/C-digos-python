from queue import Queue

def main():
    p, a = [int(x) for x in input().split()]
    ID = -1 # identificação de cada letra no dicionário
    dic = {}
    grafo = [[] for _ in range(4010)]
    passou = [False for _ in range(4010)] #guarda o processamento dos pontos
    
    for _ in range(a):
        p1, p2 = input().split()
        
        try:
            u = dic[p1]
        except KeyError:
            ID += 1
            dic[p1] = u = ID
            if p1 == '*': queijo = u
            if p1 == 'Entrada': entrada = u
            if p1 == 'Saida': saida = u
            
        try:
            v = dic[p2]
        except KeyError:
            ID += 1
            dic[p2] = v = ID
            if p2 == '*': queijo = v
            if p2 == 'Saida': saida = v
            if p2 == 'Entrada': entrada = v
            
        grafo[u].append(v)
        grafo[v].append(u)
        
    print(BFS(queijo, grafo, passou, entrada, saida))


        
def BFS(fonte, grafo, passou, entrada, saida):
    fila = Queue()
    fila.put((0, fonte))
    passou[fonte] = True
    resposta = 0
    
    while not fila.empty():
        visitados, u = fila.get()
        
        for v in grafo[u]:
            if not passou[v]:
                passou[v] = True
                fila.put((visitados + 1, v))
                
        if entrada == u or saida == u:
            resposta += visitados

    return resposta

main()
