class Pilha:
    def __init__(self):
        self.elem = []
        self.size = 0

    def push(self, x):
        self.elem.append(x)
        self.size += 1

    def pop(self):
        del self.elem[-1]
        self.size -= 1
        
    def top(self):
        return self.elem[-1]

def main():
    n = int(input())
    numeros = [int(x) for x in input().split()]
    resposta = [-1]

    p = Pilha()
    p.push(numeros[-1])

    for i in range(len(numeros) - 2, -1, -1):
        while p.size > 0:
            if numeros[i] >= p.top():
                p.pop()
            else:
                break
        if p.size == 0:
            resposta.append(-1)
        else:
            resposta.append(p.top())
        p.push(numeros[i])

    print(' '.join([str(x) for x in resposta[::-1]]))
        
main()
