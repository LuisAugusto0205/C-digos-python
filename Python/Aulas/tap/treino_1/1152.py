class Disjoints_sets:
    def __init__(self, n):
        self.nodes = [i for i in range(n)]
        self.qnt = [1 for _ in range(n)]

    def find(self, u):
        if self.nodes[u] != u:
            self.nodes[u] = self.find(self.nodes[u])

        return self.nodes[u]

    def same_set(self, x, y):
        if self.find(x) == self.find(y):
            #print('{} e {} estão no mesmo conjunto'.format(x, y))
            return True
        #print('{} e {} não estão no mesmo conjunto'.format(x, y))
        return False

    def merge(self, x, y):
        #print('juntando cojunto do {} e {} '.format(x, y))
        x = self.find(x)
        y = self.find(y)

        if self.qnt[x] < self.qnt[y]:
            x, y = y, x

        self.nodes[y] = x
        self.qnt[x] += self.qnt[y]

def main():
    m, n = [int(x) for x in input().split()]

    while n > 0 and m > 0:
        maximo = minimo = 0
        arestas = []
        caminho = []
        
        for _ in range(n):
            u, v, z = [int(x) for x in input().split()]
            maximo += z
            arestas.append((z, (u, v)))

        arestas.sort()

        Kruskal(arestas, caminho, n, m)

        for aresta in caminho:
            minimo += aresta[0]
        #print('max: {} min: {}'.format(maximo, minimo))
        #print(caminho) 
        print(maximo - minimo)
        m, n = [int(x) for x in input().split()]         

def Kruskal(arestas, caminho, n, m):
    ds = Disjoints_sets(m)

    for aresta in arestas:
        p = aresta[0]
        u = aresta[1][0]
        v = aresta[1][1]

        if not ds.same_set(u, v):
            ds.merge(u, v)
            caminho.append(aresta)

        if len(caminho) == m - 1:
            break

main()
        
