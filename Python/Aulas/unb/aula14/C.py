def main():
    minutos = [int(x) for x in input().split()]
    erradas = [int(x) for x in input().split()]
    Hs, Hf = [int(x) for x in input().split()]
    x = [500, 1000, 1500, 2000, 2500]

    soma = sum([max(0.3*x[i], (1 - minutos[i]/250)*x[i] - 50*erradas[i]) for i in range(5)])

    score = soma + Hs*100 - Hf*50
    print(int(score))

main()
