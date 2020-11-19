class Union_find():
    def __init__(self, n):
        self.nodes = [i for i in range(n)]
        self.qnt = [1] * n

    def find(self, u):
        if self.nodes[u] != u:
            self.nodes[u] = self.find(self.nodes[u])

        return self.nodes[u]

    def merge(self, x, y):
        x = self.find(x)
        y = self.find(y)

        x, y = max(x, y), min(x, y)

        self.nodes[y] = x
        self.qnt[x] += self.qnt[y]
    
def main():
    n, m = [int(x) for x in input().split()]
    arestas = []

    for _ in range(m):
        u, v, p = [int(x) for x in input().split()]
        u -= 1
        v -= 1
        
        arestas.append([p, (u, v)])

    arestas.sort()

    resposta = kruskal(arestas, n)

    print(resposta)
    
def kruskal(arestas, n):
    ds = Union_find(n)
    c = 0
    resposta = 0
    for aresta in arestas:
        p = aresta[0]
        u = aresta[1][0]
        v = aresta[1][1]

        if ds.find(u) != ds.find(v):
            ds.merge(u, v)
            c += 1
            resposta += p

        if c == n - 1:
            return resposta

main()
