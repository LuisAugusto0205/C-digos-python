comb_m = 0
peso_m = 0
ganho_m = 0

def main():
    global comb_m
    capacidade, n = [int(x) for x in input().split()]
    itens = [tuple([int(x) for x in input().split()]) for _ in range(n)]

    combination(['']*n, 0, 1, capacidade, itens)

    for i in range(len(comb_m)):
        if comb_m[i]: print('item {}'.format(i + 1))
    
    comb_m = 0
    peso_m = 0
    ganho_m = 0

def combination(comb, pos, valor, cap, itens):
    global comb_m, peso_m, ganho_m
    #base
    if pos < len(comb):
        if valor != comb[pos]: comb[pos] = valor
        else: return
    else:
        melhor(comb, cap, itens)
        return

    combination(comb, pos + 1, 1, cap, itens)
    combination(comb, pos, 0, cap, itens)

def melhor(comb, cap, itens):
    global comb_m, peso_m, ganho_m
    peso = 0
    ganho = 0
    
    for i in range(len(comb)):
        if comb[i] == 1:
            peso += itens[i][0]
            ganho += itens[i][1]

    if peso <= cap and ganho > ganho_m:
        peso_m = peso
        ganho_m = ganho
        comb_m = comb[:]
            
