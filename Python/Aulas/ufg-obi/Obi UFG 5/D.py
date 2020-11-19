class Burger:
    def __init__(self, qntd, valor):
        self.qntd = qntd
        self.valor = valor

def main():
    t = int(input())
    for _ in range(t):
        p, b, f = [int(x) for x in input().split()]
        h, c = [int(x) for x in input().split()]
        s = p//2
        B  = [Burger(f, c), Burger(b, h)]
        print(solve(B, s))

def solve(B, s):
    B.sort(key = lambda B: B.valor, reverse = True)
    resto = s - B[0].qntd
    if B[0].qntd >= s:
        return s*B[0].valor
    elif B[1].qntd >= resto :
        return B[0].qntd * B[0].valor + resto * B[1].valor
    else:
        return B[0].qntd * B[0].valor + B[1].qntd * B[1].valor 

main()
