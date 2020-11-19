def main():
    #dados de entrada
    k, r = [int(x) for x in input().split()]
    print(solve(k, r))

def solve(k, r):
    quantidade_pa = 1
    aux = k
    while True:
        unidade = aux%10 
        if unidade == 0 or unidade == r:
            return quantidade_pa
        quantidade_pa += 1
        aux += k

main()
