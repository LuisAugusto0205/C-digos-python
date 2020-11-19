def main():
    n = int(input())
    numeros = [int(x) for x in input().split()]
    mdc = 0

    for numero in numeros:
        mdc = MDC(mdc, numero)

    print(mdc)
    
def MDC(a, b):
    return (a if b == 0 else MDC(b, a%b))

main()
