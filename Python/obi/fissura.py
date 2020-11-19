#python 3
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
    n, f = [int(x) for x in input().split()]
    mapa = []
    passou = [[False]*(n + 10) for _ in range(n + 10)]
    
    for _ in range(n):
        linha = [x for x in input()]
        mapa.append(linha)

    BFS(0, 0, mapa, passou, f, n)

    for i in range(n):
        for j in range(n):
            if j == n - 1:
                print(mapa[i][j])
            else:
                print(mapa[i][j], end = '')
    
        
        
def BFS(x, y, mapa, passou, f, n):
    fila = Fila()
    if int(mapa[x][y]) <= f:
        fila.push((x, y))
        passou[x][y] = True
        mapa[x][y] = '*'
        
    while fila.size > 0:
        x, y = fila.front()
        fila.pop()

        if x + 1 < n and not passou[x + 1][y] and f >= int(mapa[x + 1][y]):
            passou[x + 1][y] = True
            fila.push((x + 1, y))
            mapa[x + 1][y] = '*'

        if x - 1 >= 0 and not passou[x - 1][y] and f >= int(mapa[x - 1][y]):
            passou[x - 1][y] = True
            fila.push((x - 1, y))
            mapa[x - 1][y] = '*'

        if y + 1 < n and not passou[x][y + 1] and f >= int(mapa[x][y + 1]):
            passou[x][y + 1] = True
            fila.push((x, y + 1))
            mapa[x][y + 1] = '*'

        if y - 1 >= 0 and not passou[x][y - 1] and f >= int(mapa[x][y - 1]):
            passou[x][y - 1] = True
            fila.push((x, y - 1))
            mapa[x][y - 1] = '*'


main()   
