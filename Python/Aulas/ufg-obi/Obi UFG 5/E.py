def main():
    m = input()
    c = input()
    print(solve(m, c))

def solve(m, c):
    pos = 0
    t_c, t_m = len(c), len(m)
    for i in range(t_c, t_m+1):
        slice_m = m[i-t_c:i]
        for j in range(t_c):
            igual = False
            if slice_m[j] == c[j]:
                igual = True
                break
        if not igual: pos += 1
    return pos

main()
