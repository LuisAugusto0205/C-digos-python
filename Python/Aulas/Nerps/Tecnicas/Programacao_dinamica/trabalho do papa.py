import bisect
class Caixa:
    def __init__(self, peso, res):
        self.peso = peso
        self.res = res
        self.pos = 0

def main():
    n = int(input())
    caixas = [Caixa(*[int(x) for x in input().split()]) for _ in range(n)]
    caixas.sort(key = lambda caixa: caixa.peso)
    
    pesos_soma = [caixas[i].peso]
    for i in range(1, len(caixas)):
        pesos_soma.append(caixas[i - 1].peso + caixas[i].peso)
        caixas[i].pos = i
    
    for base in caixas:
        j = bisect.bisect_left(pesos_soma, base.res)
        if pesos_soma[j] > base.res: j -= 1
        
        if base.pos > j:
            j = bisect.bisect_left(pesos_soma, base.res - base.peso)
            if pesos_soma[j] > base.res: j -= 1
            copia_ps = pesos_soma[:j+1]
        else:
            copia_ps = pesos_soma[:base.pos] + pesos_soma[base.pos + 1: j + 1]
            for z in range(base.pos, j):
                copia_ps[z] -= base.peso

        copia_res = sorted(copia_ps, key = lambda caixa: caixa.res)

        while copia_res:
            if copia_ps[-1] >= 
