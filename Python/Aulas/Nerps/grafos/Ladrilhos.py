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
    
    l, c = [int(x) for x in input().split()]
    ladrilhos = [input().split() for _ in range(l)]
    passou = [[False]*201 for _ in range(201)]

    menor_area = 40010
    
    for i in range(l):
        for j in range(c):
            if not passou[i][j]:
                passou[i][j] = True
                qnt = BFS(i, j, ladrilhos, l, c, passou)
                if qnt < menor_area:
                    menor_area = qnt

    print(menor_area)

def BFS(x, y, ladrilhos, l, c, passou):

    fila = Fila()
    fila.push([x, y])
    qnt = 1
    
    while fila.size > 0:
        x, y = fila.front()
        fila.pop()
        
        if x + 1 < l and ladrilhos[x][y] == ladrilhos[x + 1][y] and not passou[x + 1][y]:
            passou[x + 1][y] = True
            qnt += 1
            fila.push([x + 1, y])
        
        if x - 1 >= 0 and ladrilhos[x][y] == ladrilhos[x - 1][y] and not passou[x - 1][y]:
            passou[x - 1][y] = True
            qnt += 1
            fila.push([x - 1, y])
            
        if y + 1 < c and ladrilhos[x][y] == ladrilhos[x][y + 1] and not passou[x][y + 1]:
            passou[x][y + 1] = True
            qnt += 1
            fila.push([x, y + 1])

        if y - 1 >= 0 and ladrilhos[x][y] == ladrilhos[x][y - 1] and not passou[x][y - 1]:
            passou[x][y - 1] = True
            qnt += 1
            fila.push([x, y - 1])
    
    return qnt

    
'''def DFS(x, y, ladrilhos, l, c, passou):
    qnt = 1
    
    if x + 1 < l and ladrilhos[x][y] == ladrilhos[x + 1][y] and not passou[x + 1][y]:
        passou[x + 1][y] = True
        qnt += DFS(x + 1, y, ladrilhos, l, c, passou)
        
    if x - 1 >= 0 and ladrilhos[x][y] == ladrilhos[x - 1][y] and not passou[x - 1][y]:
        passou[x - 1][y] = True
        qnt += DFS(x - 1, y, ladrilhos, l, c, passou)
        
    if y + 1 < c and ladrilhos[x][y] == ladrilhos[x][y + 1] and not passou[x][y + 1]:
        passou[x][y + 1] = True
        qnt += DFS(x, y + 1, ladrilhos, l, c, passou)

    if y - 1 >= 0 and ladrilhos[x][y] == ladrilhos[x][y - 1] and not passou[x][y - 1]:
        passou[x][y - 1] = True
        qnt += DFS(x, y - 1, ladrilhos, l, c, passou)

    return qnt'''

main()
