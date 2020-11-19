class Union_find:
    def __init__(self, n):
        self.nodes = [i for i in range(n)]
        self.ranks = [0 for _ in range(n)]

    def find(self, u):
        if u != self.nodes[u]:
            self.nodes[u] = self.find(self.nodes[u])

        return self.nodes[u]

    def merge(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if self.ranks[x] > self.ranks[y]:
            self.nodes[y] = x
        else:
            self.nodes[x] = y

        if self.ranks[x] == self.ranks[y]:
            self.ranks[y] += 1

def main():
    n, m, p = [int(x) for x in input().split()]
    bairros = Union_find(n)

    for _ in range(m):
        a, b = [int(x) - 1 for x in input().split()]
        bairros.merge(a, b)

    for _ in range(p):
        k, l = [int(x) - 1 for x in input().split()]
        if bairros.find(k) == bairros.find(l):
            print('Lets que lets')
        else:
            print('Deu ruim')

main()
        
        
