import sys
sys.setrecursionlimit(10**5 + 1)

def main():
    global n, peso, dp, k

    n, k = [int(x) for x in input().split()]
    peso = [int(x) for x in input().split()]
    dp = [-1]*(10**5 + 1)
    
    peso.append(10**9)
    peso.append(10**9)
    
    print(frog(0))
    
def frog(i):
    global n, peso, dp, k
    
    if i >= n - 1:
        return 0

    if dp[i] != -1:
        return dp[i]
    
    dp[i] = 10**9
    for j in range(1, k + 1):
        if i + j < len(peso):
            dp[i] = min(dp[i], abs(peso[i + j] - peso[i]) + frog(i + j))
    
    return dp[i]

main()
