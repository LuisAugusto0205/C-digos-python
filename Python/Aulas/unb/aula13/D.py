def main():
    n = int(input())
    chess = [tuple([int(x) for x in input().split()]) for _ in range(n)]
    m = int(input())
    prog = [tuple([int(x) for x in input().split()]) for _ in range(m)]
    print(solve(chess, prog))

def solve(chess, prog):
    chess.sort(key = lambda c: c[1])
    prog.sort(key = lambda p: p[0])
    rest1 = prog[-1][0] - chess[0][1]
    chess.sort(key = lambda c: c[0])
    prog.sort(key = lambda p: p[1])
    rest2 = chess[-1][0] - prog[0][1]
    if rest1 < 0 and rest2 < 0:
        return 0
    elif rest1 < 0:
        rest = rest2
    elif rest2 < 0:
        rest = rest1
    else:
        rest = min(rest1, rest2)
    return rest
main()
