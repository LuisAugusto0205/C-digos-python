import bisect
class num:
    def __init__(self, num, pos_i):
        self.num = int(num)
        self.pos_i = pos_i
    def __lt__(self, other):
        return self.num < other
    def __gt__(self, other):
        return self.num > other
    def __eq__(self, other):
        return self.num == other
    
def main():
    n = int(input())
    lista = [num(x, i) for i, x in enumerate(input().split())]
    m = [int(x) for x in input().split()]
    buscas = [int(x) for x in input().split()]
    print(solve(n, lista, m, buscas))

def solve(n, lista, m, buscas):
    lista.sort(key = lambda n: n.num)
    comp_v = 0
    comp_p = 0
    for q in buscas:
        a = bisect.bisect_left(lista, q)
        comp_v += lista[a].pos_i + 1
        comp_p += (n - lista[a].pos_i)
    return '{} {}'.format(comp_v, comp_p)

main()
