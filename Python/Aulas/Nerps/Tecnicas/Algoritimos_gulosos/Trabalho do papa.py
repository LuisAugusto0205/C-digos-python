def main():
    #leitura dos dados
    numero_caixas = int(input())
    caixas = [tuple([int(x) for x in input().split()]) for _ in range(numero_caixas)]# gera uma lista de tuplas

    caixas.sort(
