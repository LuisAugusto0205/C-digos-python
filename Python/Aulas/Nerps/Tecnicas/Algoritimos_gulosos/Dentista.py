class Horario:
    def __init__(self, ini, fim):
        self.ini = ini
        self.fim = fim
    def __lt__(self, other):
        if self.fim <= other.fim:
            return True
        else:
            return False
    def __repr__(self):
        return '{}-{}'.format(self.ini, self.fim)

def main():
    n = int(input())
    consultas = []
    for _ in range(n):
        i, f = [int(x) for x in input().split()]
        consultas.append(Horario(i, f))
    print(solve(consultas, n))

def solve(agenda, n):
    agenda.sort()#O(n*log n) timsort
    termino = agenda[0].ini
    qnt_consulta = 0
    for i in range(n):#O(n) percorre a lista
        consulta = agenda[i]
        if termino <= consulta.ini:
            termino = consulta.fim
            qnt_consulta += 1
    return qnt_consulta
        
main()
