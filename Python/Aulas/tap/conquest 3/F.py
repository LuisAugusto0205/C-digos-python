def main():
    n = int(input())
    pedras = input()

    r = 0
    for p in pedras:
        if p == 'R':
            r += 1

    st2 = 'R'*r + 'W'*(n - r)

    resp = 0

    for i in range(n):
        if pedras[i] == 'R' and st2[i] == 'W':
            resp += 1

    print(resp)
main()
        
            
