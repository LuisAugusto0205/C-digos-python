def main():
    a, b, c, d = [int(x) for x in input().split()]
    denominador = b*d
    numerador = a*d + c*b

    s = MDC(numerador, denominador)
    numerador, denominador = numerador//s, denominador//s

    print(numerador, denominador)

def MDC(a, b):
    return (a if not b else MDC(b, a%b))

main()
