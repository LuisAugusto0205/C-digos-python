prob = []
lim = tam = 0
dp = []
import sys
sys.setrecursionlimit(100000)

def main():
    global prob, lim, dp, tam
    tam = int(input())
    lim = tam//2 + 1
    
    prob = [float(x) for x in input().split()]
    dp = [[-1]*(tam + 1) for _ in range(tam + 1)]
    
    print(coins(0, 0))
    
def coins(n, k):
    global prob, lim, dp, tam
    
    if n == tam:
        if k >= lim:
            return 1
        else:
            return 0

    if dp[n][k] != -1:
        return dp[n][k]
    
    dp[n][k] = coins(n + 1, k)*(1 - prob[n-1]) + coins(n + 1, k + 1)*prob[n-1]
    return dp[n][k]


        
main()
