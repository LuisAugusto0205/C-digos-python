def main():
    n = int(input())
    lista = [int(x) for x in input().split()]
    resposta = lista[0]
    for num in lista:
        resposta |= num
    print(resposta)
main()
