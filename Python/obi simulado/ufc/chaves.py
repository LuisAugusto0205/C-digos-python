class Pilha:
    def __init__(self):
        self.elem = []
        self.size = 0

    def coloca(self, i):
        self.elem.append(i)
        self.size += 1
        
    def tira(self):
        del self.elem[-1]
        self.size -= 1

def main():
    n = int(input())
    codigo = ''

    for _ in range(n):
        linha = input()
        codigo += linha

    abertas = Pilha()

    for i in range(len(codigo)):
        if codigo[i] == '{':
            abertas.coloca(i)
        elif codigo[i] == '}':
            if abertas.size > 0:
                abertas.tira()
            else:
                print('N')
                return

    if abertas.size == 0: print('S')
    else: print('N')

main()
