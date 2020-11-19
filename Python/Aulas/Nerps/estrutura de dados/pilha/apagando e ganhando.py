from sys import stdin
class stack:
    def __init__(self):
        self.elem = []
        self.size = 0

    def push(self, x):
        self.elem.append(x)
        self.size += 1

    def top(self):
       return self.elem[-1]

    def pop(self):
        del self.elem[-1]
        self.size -= 1

    def Size(self):
        return self.size

def main():
    n, r = [int(x) for x in input().split()]
    pilha = stack()
    tamanho = pilha.Size
    topo = pilha.top
    deletar = pilha.pop
    colocar = pilha.push
    readline = stdin.readline
    
    while n > 0 and r > 0:
        apagados = 0
        
        for _ in range(n):
            num = readline(1)
            while tamanho() > 0 and apagados < r and num > topo():
                deletar()

                apagados += 1

            if tamanho() < n - r: colocar(num)

        print(''.join(pilha.elem))
        readline()
        pilha.elem = []
        pilha.size = 0
            
        n, r = [int(x) for x in input().split()]
    
main()
