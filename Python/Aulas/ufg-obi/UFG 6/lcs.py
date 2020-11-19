dp = []
def maior(a, b):
    if len(a) > len(b):
        return a
    else:
        return b

def lcs(i, j, a, b):
    global dp
    if i >= len(a) or j >= len(b):
        return ''

    if dp[i][j] is not None:
        return dp[i][j]

    if a[i] == b[j]:
        dp[i][j] = a[i] + lcs(i + 1, j + 1, a, b)
        return dp[i][j]
    
    dp[i][j] = maior(lcs(i + 1, j, a, b),
                     lcs(i, j + 1, a, b))
    return dp[i][j]

def main():
    global dp
    a = input()
    b = input()
    
    dp = [[None]*len(b) for _ in range(len(a))]

    print(lcs(0, 0, a, b))

main()
