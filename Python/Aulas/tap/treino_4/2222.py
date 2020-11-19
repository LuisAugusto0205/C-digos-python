def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        m = []
        
        for i in range(n):
            s = set()
            aux = [int(x) for x in input().split()][1:]
            for elem in aux:
                s.add(elem)
            m.append(s)

        q = int(input())

        for w in range(q):
            op, i, j = [int(x) - 1 for x in input().split()]
            if op == 0:
                print(len(m[i].intersection(m[j])))
            else:
                print(len(m[i].union(m[j])))

main()
