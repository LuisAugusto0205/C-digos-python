class Disjuncts:
    def __init__(self, n):
        self.nodes = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, u):

        if u != self.nodes[u]:
            self.nodes[u] = self.find(self.nodes[u])

        return self.nodes[u]

    def merge(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if self.rank[x] > self.rank[y]:
            self.nodes[y] = x # atualiza para onde y aponta
        else:
            self.nodes[x] = y # atualiza para onde x aponta

        if self.rank[x] == self.rank[y]:
            self.rank[y] += 1


def main():
    p, r = [int(x) for x in input().split()]
    dic = {}
    nomes = set()
    ID = 0
    resposta = 1
    pessoas = Disjuncts(p)
    
    for _ in range(r):
        relacao = input().split()
        p1 = relacao[0]
        p2 = relacao[2]

        if p1 not in nomes:
            nomes.add(p1)
            dic[p1] = ID
            ID += 1
        if p2 not in nomes:
            nomes.add(p2)
            dic[p2] = ID
            ID += 1

        pessoas.merge(dic[p1], dic[p2])

    ant = pessoas.find(0)
    usados = [ant]
    for i in range(1, p):

        atual = pessoas.find(i)
        if atual != ant and atual not in usados:
            resposta += 1
            ant = atual
            usados.append(ant)
        
    print(resposta)

main()
