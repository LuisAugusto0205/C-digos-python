from math import log as ln

def main():
    n = int(input())

    minimo =  n/ln(n)
    maximo = 1.25506*(n/ln(n))

    print('{:.1f} {:.1f}'.format(minimo, maximo))

main()
