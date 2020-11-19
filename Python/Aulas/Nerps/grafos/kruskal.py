class UFDS():
    def __init__(self, n):
        self.pai = [i for i in range(n)]
        self.peso = [1]*n
        self.conjuntos = n

    def find(self, u):
        if self.pai[u] != u:
            self.pai[u] = self.find(self.pai[u])

        return self.pai[u]

    def merge(self, u, v):

        if self.peso[u] < self.peso[v]:
            u, v = v, u

        self.peso[u] += self.peso[v]
        self.pai[v] = u
        self.conjuntos -= 1
    
def main():
    n, f, r = [int(x) for x in input().split()]
    arestasF = []
    arestasR = []
    mst = []
    ds = UFDS(n)
    
    for i in range(f):
        u, v, p = [int(x) for x in input().split()]
        u -= 1
        v -= 1
        arestasF.append((p, [u, v]))

    for i in range(r):
        u, v, p = [int(x) for x in input().split()]
        u -= 1
        v -= 1
        arestasR.append((p, [u, v]))
        
    arestasR.sort()
    arestasF.sort()
    
    soma = kruskal(arestasF, ds)
    soma += kruskal(arestasR, ds)

    print(soma)
    
def kruskal(arestas, ds):
    soma = 0
    for aresta in arestas:
        if ds.conjuntos == 1: return soma
        u = ds.find(aresta[1][0])
        v = ds.find(aresta[1][1])

        if u != v:
            ds.merge(u, v)
            soma += aresta[0]

    return soma

            

        
    
