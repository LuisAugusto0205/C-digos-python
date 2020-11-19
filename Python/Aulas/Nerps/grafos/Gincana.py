class Fila:
    def __init__(self):
        self.elem = []
        self.size = 0

    def push(self, x):
        self.elem.append(x)
        self.size += 1

    def pop(self):
        del self.elem[0]
        self.size -= 1

    def front(self):
        return self.elem[0]

def main():
    #leitura dos dados
    a, r = [int(x) for x in input().split()]
    amizade = [[] for _ in range(1010)]
    grupinhos = ['']*1010
    
    for _ in range(r):
        u, v = [int(x) for x in input().split()]
        amizade[u].append(v)
        amizade[v].append(u)

    resposta = 0

    for i in range(1, a + 1):
        if grupinhos[i] == '':
            resposta += 1
            BFS(i, amizade, grupinhos, resposta)

    print(resposta)
    
def BFS(v, amizade, grupinhos, valor):#passa por todas vertices de uma componente conexa
    fila = Fila()

    fila.push(v)
    grupinhos[v] = valor

    while fila.size > 0:

        v = fila.front()
        fila.pop()

        for u in amizade[v]:
            if grupinhos[u] == '':
                grupinhos[u] = valor
                fila.push(u)

main()






    
