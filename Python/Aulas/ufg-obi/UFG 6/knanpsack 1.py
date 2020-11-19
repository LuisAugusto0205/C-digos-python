def main():
    n, w = [int(x) for x in input().split()]
    itens = []
    dp = [[-1]*w for i in range(n)]
    
    for _ in range(n):
        itens.append([int(x) for x in input().split()])#item([peso, valor])

    print(knapsack(n, w, itens, dp))

def knapsack(n, w, itens, dp):

    if n == 0 or w == 0:
        return 0

    if dp[n-1][w-1] != -1:
        return dp[n-1][w-1]

    if itens[n-1][0] > w:
        dp[n-1][w-1] = knapsack(n-1, w, itens, dp)
        return dp[n-1][w-1]

    else:
        dp[n-1][w-1] = max(itens[n-1][1] + knapsack(n-1, w - itens[n-1][0], itens, dp),
                           knapsack(n-1, w, itens, dp))

        return dp[n-1][w-1]

main()
    
