def main():
    while True:
        try:
            n, l, u = [int(x) for x in input().split()]
            print(solve(n, l, u))
        except EOFError:
            break

def solve(n, l, u):
    Max = n | l
    res = l
    for m in range(l+1, u+1):
        x = n | m
        if x > Max:
            res = m
            Max = x
    return res
        
main()
