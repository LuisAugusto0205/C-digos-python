class Fila:
    def __init__(self):
        self.elem = []
        self.size = 0

    def pop(self):
        del self.elem[0]
        self.size -= 1

    def push(self, x):
        self.elem.append(x)
        self.size += 1

    def front(self):
        return self.elem[0]
    
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
        
    resposta = BFS(i_3, valores, salas)
    print(resposta)
    
def BFS(v, valores, salas):

    cont = 0
    fila = Fila()

    fila.push(v)

    while fila.size > 0:
        v = fila.front()
        fila.pop()

        for u in salas[v]:
            if valores[u] == '1':
                cont += 1
                valores[u] = '0'
                fila.push(u)
            elif valores[u] == '2':
                return cont + 2
main()





