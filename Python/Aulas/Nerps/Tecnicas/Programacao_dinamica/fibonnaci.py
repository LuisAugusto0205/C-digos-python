vetor = []
for i in range(10**10000000):
    vetor.append(-1)

def fib_topdown(n):
    if  vetor[n] != -1:
        return  vetor[n]
    if n == 0: return 0
    if n == 1: return 1
    vetor [n] = fib_topdown(n-1) + fib_topdown(n-2)
    return vetor[n]

def fib_bottomup(n):
    l_fib = []
    l_fib.append(0)
    l_fib.append(1)
    for i in range(2, n+1):
        l_fib.append(l_fib[i-1]+l_fib[i-2])
    return l_fib[n]
