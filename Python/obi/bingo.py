import bisect
def main():
    n, k, u = [int(x) for x in input().split()]
    cartelas = [None]
    falta = [None]
    ganhadores = []
    for _ in range(n):
        cartela = [int(x) for x in input().split()]
        cartela.sort()
        cartelas.append(cartela)
        falta.append(k)
    
    sequencia = [int(x) for x in input().split()]
    
    for davez in sequencia:
        for i in range(1, n + 1):
            j1 = bisect.bisect_right(cartelas[i], davez)
            j2 = bisect.bisect_left(cartelas[i], davez)
            if j1 != j2:
                falta[i] -= 1
                if not falta[i]: ganhadores.append(i)

        if len(ganhadores) > 0:
            print(' '.join([str(x) for x in ganhadores]))
            break
main()
