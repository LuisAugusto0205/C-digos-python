def main():
    n, m = [int(x) for x in input().split()]
    faixas = [int(x) for x in input().split()]
    premio = [int(x) for x in input().split()]
    st = ''
    for x in input().split():
        i = busca_bin(faixas, int(x))
        st += str(premio[i]) + ' '
    print(st[:-1])

def busca_bin(v, x):
    s = len(v) - 1
    i = 0
    resp = len(v)
    while s >= i:
        m = (s+i)//2
        if v[m] > x:
            resp = m
            s = m - 1
        else:
            i = m + 1
    return resp

main()
