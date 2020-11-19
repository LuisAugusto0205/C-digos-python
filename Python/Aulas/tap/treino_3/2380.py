class UFDS:
    def __init__(self, n):
        self.bancos = [i for i in range(n + 1)]
        self.qnt = [1]*(n + 1)

    def find(self, n):
        if self.bancos[n] != n:
            self.bancos[n] = self.find(self.bancos[n])

        return self.bancos[n]

    def merge(self, a, b):
        a = self.find(a)
        b = self.find(b)

        if a != b:
            if self.qnt[b] > self.qnt[a]:
                a, b = b, a

            self.qnt[a] += self.qnt[b]
            self.bancos[b] = a

def main():
    n, k = [int(x) for x in input().split()]
    sistema = UFDS(n)
    
    for _ in range(k):
        op, a, b = input().split()

        if op == 'C':
            if sistema.find(int(a)) == sistema.find(int(b)):
                print('S')
            else:
                print('N')
        else:
            sistema.merge(int(a), int(b))

main()
