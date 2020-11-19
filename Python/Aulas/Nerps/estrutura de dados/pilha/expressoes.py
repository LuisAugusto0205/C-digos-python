from queue import LifoQueue
abre = ['{', '[', '(']
fecha = ['}', ']', ')']
def main():
    t = int(input())
    for _ in range(t):
        ok = True
        expr = input()
        pilha = LifoQueue()
        for char in expr:
            if char in abre:
                pilha.put(char)
            elif char in fecha:
                if not pilha.empty():
                    topo = pilha.get()
                else:
                    ok = False
                    break
                if abre.index(topo) != fecha.index(char):
                    ok = False
                    break
        if not pilha.empty():
            ok = False
        
        if ok:
            print('S')
        else:
            print('N')
main()
