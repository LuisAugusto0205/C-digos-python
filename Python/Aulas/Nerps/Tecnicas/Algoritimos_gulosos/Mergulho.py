def main():
    n, m = [int(x) for x in input().split()]
    mergulhos = [int(x) for x in input().split()]
    print(solve(n, m, mergulhos))

def solve(n, m, mergulhos):
    for i in range(n):
        if mergulhos[i] >= m/2:
            mergulhos[i] = m - mergulhos[i]
        if i > 0:
           if mergulhos[i] < mergulhos[i-1]:
               mergulhos[i] = m - mergulhos[i]
               if mergulhos[i] < mergulhos[i-1]:
                    return -1
    return sum(mergulhos)
                
