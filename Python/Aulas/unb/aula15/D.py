class time:
    def __init__(self, acertos, tempo):
        self.acertos = acertos
        self.tempo = tempo

    def __repr__(self):
        return '{} {}'.format(self.acertos, self.tempo)
    
    def __eq__(self, other):
        return self.acertos == other.acertos and self.tempo == other.tempo
        
    def __lt__(self, other):
        if self.acertos < other.acertos:
            return True
        elif self.acertos == other.acertos:
            if self.tempo > other.tempo:
                return True
            else:
                return False
        else: return False

def main():
    n, k = [int(x) for x in input().split()]
    table = sorted([time(*[int(x) for x in input().split()]) for _ in range(n)])[::-1]

    print(solve(table, n, k))

def solve(table, n, k):
    resposta = 1
    aux1 = aux2 = k-1
    while n-1 > aux1 and table[aux1] == table[aux1+1]:
        resposta += 1
        aux1 += 1
        if aux1 == len(table) - 1: break
    while 0 < aux1 and table[aux2] == table[aux2-1]:
        resposta += 1
        aux2 -= 1
        if aux2 == 0: break
    return resposta

main()
