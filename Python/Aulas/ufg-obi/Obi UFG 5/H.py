import math
class pilha:
    def __init__(self):
        elem = []
        alterada = False
        size = 0
    
    def pop(self):
        if self.size == 0:
            raise IndexError('não há elementos na pilha')
        del elem[size - 1]
        size -= 1
        
    def push(self, x):
        alterada = True
        elem.append(x)
        size += 1

    def empty(self):
        return self.size == 0

    def top(self):
        if self.size == 0:
            raise IndexError('não há elementos no topo')
        return elem[size]
    
    def sec(self):
        if self.size < 2:
            raise IndexError('não há elementos na segunda posição')
        return elem[size-2]

def main():
    st1 = input()
    st2 = input()
    funcs = ['concat', 'sort', 'suffle']
    p = pilha()
    for i in range(len(st1)):
        prob = 0
        tamanho = 0
        if st1[i] == '(':
            p.push(i)
        elif st1[i] == ')':
            if p.size == 1:
                func = st1[:p.top]
            else:
                func = st1[p.sec + 1:p.top]
                if func == funcs[2]:
                    L = len(st1[p.top + 2: i-1])
                    tamanho
                    S = set(L)
                    prob = 
                    
