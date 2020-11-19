def main():
    n, m = [int(x) for x in input().split()]
    fechadura = [int(x) for x in input().split()]
    print(solve(n, m, fechadura))

def solve(n, m, fechadura):
    acoes = 0
    for i in range(n-1): #O(n)
        if fechadura[i] > m:
            acoes += fechadura[i] - m
            fechadura[i + 1] -= fechadura[i] - m
        elif fechadura[i] == m:
            continue
        else:
            acoes += m - fechadura[i] 
            fechadura[i + 1] += m - fechadura[i]
    return acoes

main()
