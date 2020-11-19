def mdc(a, b):
    if b == 0: return a
    return mdc(b, a%b)

def main():
    resp = 0
    k = int(input())
    for i in range(1, k + 1):
        for j in range(1, k + 1):
            for w in range(1, k + 1):
                resp += mdc(mdc(i, j), w)

    print(resp)
                
    
main()
