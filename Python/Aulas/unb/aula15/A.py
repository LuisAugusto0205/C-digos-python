def main():
    #leitura
    n = int(input())
    if n % 2 == 0:
        ultimo_par = n
        ultimo_impar = n-1
        soma_impar = ((1 + ultimo_impar)*(n//2))//2
        soma_par = ((2 + ultimo_par)*(n//2))//2
    else:
        ultimo_par = n-1
        ultimo_impar = n
        soma_impar = ((1 + ultimo_impar)*(n//2 + 1))//2
        soma_par = ((2 + ultimo_par)*(n//2))//2

    f = soma_par - soma_impar
    print(f)

main()
