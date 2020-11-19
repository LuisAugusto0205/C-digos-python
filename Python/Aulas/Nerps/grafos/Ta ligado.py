def main():
    n, m = [int(x) for x in input().split()]
    ilhas = [[] for _ in range(n + 10)]
    existe = False
    
    for _ in range(m):
        t, a, b = [int(x) for x in input().split()]
        a -= 1
        b -= 1
        if t:
            ilhas[a].append(b)
            ilhas[b].append(a)
        else:
            for ilha in ilhas[b]:
                if ilha == a:
                    existe = True
                    break
                
            if existe:
                print(1)
                existe = False
            else: print(0)

main()
