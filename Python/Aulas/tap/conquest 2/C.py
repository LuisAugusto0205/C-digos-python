def mdc(a, b):
    if b == 0: return a
    return mdc(b, a%b)

def main():
    n = int(input())

    for _ in range(n):
        numeros = [int(x) for x in input().split()]
        resp = 0
        for i in range(len(numeros)):
            for j in range(i + 1, len(numeros)):
                resp = max(resp, mdc(numeros[i], numeros[j]))
        print(resp)

main()
