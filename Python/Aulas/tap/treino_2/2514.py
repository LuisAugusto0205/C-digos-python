def mdc(a, b):
    if not b:
        return a
    return mdc(b, a%b)

def main():
    while True:
        try:
            m = int(input())
            a, b, c = [int(x) for x in input().split()]
            D_ab = mdc(a, b)
            M_ab = a * (b // D_ab)
            mmc = M_ab * (c // mdc(M_ab, c))
            
            print(mmc - m)
        except EOFError:
            break

main()
