achou_2 = False
def main():
    n, m  = [int(x) for x in input().split()]#n linhas e colunas
    m += 2
    n += 2
    
    salas = []
    valores = ['0']*(m*n)

    for _ in range(m*n):
        salas.append([])

    i = m - 1
    for _ in range(n - 2):
        i += 1
        
        for char in input()[::2]:
            i += 1
            if char != '0':
                salas[i].append(i - 1)
                salas[i].append(i + 1)
                salas[i].append(i - m)
                salas[i].append(i + m)
                valores[i] = char
            if char == '3': i_3 = i
        i += 1
        
    DFS(i_3, valores, 1, salas)

def DFS(v, valores, caminho, salas):
    global achou_2
    
    if achou_2:
        return
    
    for u in salas[v]:
        if achou_2: break
        if valores[u] == '1':
            valores[u] = '0'
            DFS(u, valores, caminho + 1, salas)
        elif valores[u] == '2':
            print(caminho + 1)
            achou_2 = True
            return
main()
