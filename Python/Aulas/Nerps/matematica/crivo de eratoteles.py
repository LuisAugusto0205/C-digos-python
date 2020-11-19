def main():
    n = int(input())

    naturais = [True]*(n + 1)
    naturais[0] = naturais[1] = 0
    resposta = ''
    #crivo
    for i in range(2, n + 1):
        if naturais[i]:
            resposta += '{} '.format(i)
            for j in range(2*i, n + 1, i):
                naturais[j] = False 

    print(resposta[:-1])
main()
