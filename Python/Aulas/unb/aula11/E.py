def main():
    y, k, n = [int(x) for x in input().split()]
    print(solve(y, k, n))

def solve(y, k, n):
    ini = k - (y%k)
    pos = n - y
    st = ''
    for num in range(ini, pos+1, k):
        if pos - num < k:
            st += '{}'.format(num)
        else:
            st += '{} '.format(num)
    if not st:
        st = '-1'
    return st

main()
