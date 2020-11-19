import sys
def main():
    st = input()
    q = int(input())
    qnt_inv = 0
    for _ in range(q):
        t = sys.stdin.read(1)
        if t == '2':
            if qnt_inv % 2 == 1:
                st = st[::-1]
                qnt_inv = 0
            f, a = input().split()
            if f == '1':
                st = a + st
            else:
                st = st + a
        else:
            t = sys.stdin.read(1)
            qnt_inv += 1

    if qnt_inv > 0 and qnt_inv % 2 == 1:
        st = st[::-1]
    print(st)

main()
