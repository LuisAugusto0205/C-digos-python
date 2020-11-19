#python 3
class Paciente:
    def __init__(self, ID, i):
        self.infectado = i
        self.ID = ID
        
def main():
    n, c = [int(x) for x in input().split()]
    pacientes = []

    for _ in range(c):
        cadeia = [int(x) for x in input().split()]
        anterior = cadeia[0]
        t = cadeia[1]
        cadeia = cadeia[2:]
        
        for i in range(len(cadeia)):
            pacientes.append(Paciente(cadeia[i], anterior))
            anterior = cadeia[i]

    pacientes.sort(key = lambda p: p.ID)

    cont = 1
    j = 0
    while cont < n + 1:
        if pacientes[j].ID == cont:
            j += 1
            cont += 1
            continue
        print(cont)
        cont += 1
        
main()
        
    
