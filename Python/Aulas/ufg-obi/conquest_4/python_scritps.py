import bisect
class Faixas:
    def __init__(self, m, pos_i):
        self.m = m
        self.pos_i = pos_i
    def __lt__(self, other):
        return self.m < other
    def __repr__(self):
        return 'M: {}'.format(self.m)
    def __gt__(self, other):
        return self.m > other
    def __eq__(self, other):
        return self.m == other
    def __add__(self, other):
        return self.m + other.m
def main():
    while True:
        try:
            faixas = [int(x) for x in input().split()]
            m, n, faixas = faixas[0], faixas[1], [Faixas(m, pos_i) for pos_i, m in enumerate(faixas[2:])]
            print(solve(m, n, faixas))
        except EOFError:
            break
        
def solve(m, n, faixas):
    ord_f = sorted(faixas)
    mais_perto = m - faixas[-1].m
    res = []
    soma = 0
    for faixa in faixas:
        s = 0
        res_t = []
        falta = m
        ord_m = ord_f[:]
        prox = bisect.bisect_left(ord_m, faixa.m)
        while True:
            s += ord_m[prox].m
            res_t.append(ord_m[prox])
            del ord_m[prox]
            falta -= faixa.m
            prox = bisect.bisect_left(ord_m, falta)
            if not ord_m: break
            elif len(ord_m) == prox: prox -= 1 #se falta for maior do que o maior elemento de ord_m
            elif ord_m[prox].m > falta: #se falta for menor do que o menor elemento de ord_m
                prox -= 1
                if prox < 0: break
            faixa = ord_m[prox]
        if falta == 0:
            soma = s
            res = res_t[:]
            break
        if mais_perto > falta:
            soma = s
            res = res_t[:]
            mais_perto = falta
    st = ' '.join([str(x.m) for x in sorted(res, key = lambda faixa: faixa.pos_i)])
    st  += ' sum:{}'.format(soma)
    return st
main()



