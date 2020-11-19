def main():
    n, m = [int(x) for x in input().split()]
    vetor = [int(x) for x in input().split()]
    for x in input().split():
        print(busca_bin(vetor, int(x), n))

def busca_bin(vetor, elem, n):
    lim_s = n-1
    lim_i = 0
    while lim_s >= lim_i:
        meio = lim_i + (lim_s - lim_i)//2
        if vetor[meio] == elem:
            return meio + 1
        elif vetor[meio] > elem:
            lim_s = meio - 1
        else:
            lim_i = meio + 1
    return -1
        
