class P_favoravel:

    def __init__(self, num, pos):
        self.num = num
        self.pos = pos
    def __repr__(self):
        return '{}'.format(self.num)
def main():
    t = int(input())
    for _ in range(t):
        linhas = []
        favs = []
        n = int(input())
        for l in range(n):
            linha = [int(x) for x in input().split()]
            m = pos_min(linha)
            favs.append(P_favoravel(linha[m], [l, m]))
            linhas.append(linha)
        favs, soma = arruma_fav(favs, linhas, n)
        print(soma)

def pos_min(lista, oc = [], n = 0, m = 0):
    for num in range(n):
        if num not in oc:
            m = num
            break
        elif num == n-1:
            return -1           
    for i in range(len(lista)):
        if i not in oc and lista[i] < lista[m]:
            m = i
    return m
    
def arruma_fav(favs, linhas, n):
    oc = []
    soma = 0
    favs.sort(key = lambda fav: fav.num)
    for i in range(len(favs)):
        l = favs[i].pos[0]
        c = favs[i].pos[1]
        if c not in oc:
            oc.append(c)
            soma += favs[i].num
        else:
            j = pos_min(linhas[l], oc, n)
            favs[i].pos[1], favs[i].num = j, linhas[l][j]
            oc.append(j)
            soma += favs[i].num
    return favs, soma
main()   
            
        
