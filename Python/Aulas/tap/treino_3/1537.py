def main():
    n = int(input())
        
    while n > 0:
        pessoas = 1
        for i in range(2, n - 2):
            pessoas = (i * pessoas)%(10**9 + 9)
        
        resp = (n * (n-1) * (n-2)) // 6
        resp %= (10**9 + 9)

        print((resp*pessoas)%(10**9 + 9))

        n = int(input())

main()
