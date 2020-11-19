def main():
    #leitura dos dados: lista de tuplas(distancia, posição) ordenadas pela distancia
    n = int(input())
    cidades = [int(x) for x in input().split()]
    print(solve(cidades, n))

def solve(cidades, n):
    menor_distancia = cidades[0]
    numero_cidade = 0
    for i in range(n):
        if cidades[i] < menor_distancia:
            menor_distancia = cidades[i]
            numero_cidade = i
    qnt = 0
    for j in range(n):
        if cidades[j] == menor_distancia:
            qnt += 1
            if qnt == 2: return 'Still Rozdil'
    return numero_cidade + 1

main()
