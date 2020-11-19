def main():
    n = int(input())
    vetor = [int(x) for x in input().split()]
    print(busca_bin(vetor, n))#procurar elemento maximo em um vetor que cresce e decrece

def busca_bin(vetor, n):
    lim_s = n-2
    lim_i = 1
    while lim_s >= lim_i:
        meio = lim_i + (lim_s - lim_i)//2
        if vetor[meio - 1] <= vetor[meio]  >=  vetor[meio + 1]:
            return meio + 1
        elif vetor[meio] > vetor[meio + 1]:
            lim_s = meio - 1
        else:
            lim_i = meio + 1
    return (vetor[0] < vetor[n-1])*(n-1) + 1
