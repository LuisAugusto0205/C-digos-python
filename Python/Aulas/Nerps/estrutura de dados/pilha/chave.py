from queue import LifoQueue

def main():
    n = int(input())
    codigo = ''
    stack = LifoQueue()
    certo = True
    
    for _ in range(n):
        codigo += input()
    
    for i, char in enumerate(codigo):
        if char == '{':
            stack.put(i)
            
        elif char == '}':
            if stack.empty():
                certo = False
                break
            
            stack.get()
            
    if not stack.empty():
        certo = False

    if certo:
        print('S')
    else:
        print('N')

main()
    
