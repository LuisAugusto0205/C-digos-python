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
    m = int(input())
    n = (1 + int((1 + 8 * m) ** 0.5))//2
    grafo = [[] for _ in range(1000)]
    Mst = []
    mst = []
    arestas = []
    maximo = minimo = 0

    for _ in range(m):
        u, v, p = [int(x) for x in input().split()]
        u -= 1
        v -= 1

        arestas.append([p, (u, v)])

    arestas.sort()
    Kruskal(arestas, mst, Mst, n, m)
    
    for i in range(n-1):
        maximo += Mst[i][0]
        minimo += mst[i][0]
            
    print(maximo)
    print(minimo)

    
def Kruskal(arestas, mst, Mst, n, m):
    ds_M = Disjoints_sets(n)
    ds_m = Disjoints_sets(n)
    
    for i in range(m):
        p_M = arestas[m - i - 1][0]
        u_M = arestas[m - i - 1][1][0]
        v_M = arestas[m - i - 1][1][1]
        p_m = arestas[i][0]
        u_m = arestas[i][1][0]
        v_m = arestas[i][1][1]

        if not ds_m.same_set(u_m, v_m):
            ds_m.merge(u_m, v_m)
            mst.append(arestas[i])

        if not ds_M.same_set(u_M, v_M):
            ds_M.merge(u_M, v_M)
            Mst.append(arestas[m - i - 1])

        if len(Mst) == n - 1 and len(mst) == n - 1:
            break
main()
