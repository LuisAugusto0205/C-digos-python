import bisect
class Ponto:
    def __init__(self, numero):
        self.numero = numero
        self.ligacoes = []

    def add(self, other):
        pos = bisect.bisect_right(self.ligacoes, other.numero)
        self.ligacoes = self.ligacoes[:pos] + [other.numero] + self.ligacoes[pos:]
    
def main():
    n, m = [int(x) for x in input().split()]
    lista_ponto = ['']*(n+1)
    for i in range(n+1):
        if i > 0: lista_ponto[i] = Ponto(i)
    for _ in range(m):
        p1, p2 = [int(x) for x in input().split()]
        lista_ponto[p1].add(lista_ponto[p2])
        lista_ponto[p2].add(lista_ponto[p1])

    l = solve(lista_ponto)
    for p in range(len(l)):
        if p == len(l) - 1:
            print(l[p])
        else:
            print(l[p], end = ' ')
            

def solve(lista_ponto):
    maior = []
    for inicial in lista_ponto:
        if inicial == '': continue
        i = 0
        ant = inicial #ponto anterior relevante
        atual = lista_ponto[ant.ligacoes[i]] # atual_intersecção
        caminho = [ant.numero, atual.numero]
        while i < len(inicial.ligacoes):
            
            pos = bisect.bisect_right(atual.ligacoes, ant.numero)
            
            if pos == len(atual.ligacoes):
                i += 1
                if i == len(inicial.ligacoes): break
                ant = inicial
                atual = lista_ponto[ant.ligacoes[i]]
                if len(caminho) > len(maior):
                    maior = caminho
            else:
                prox = lista_ponto[atual.ligacoes[pos]] # próxima_intersecção
                caminho.append(prox.numero)
                ant, atual = atual, prox
    return maior
