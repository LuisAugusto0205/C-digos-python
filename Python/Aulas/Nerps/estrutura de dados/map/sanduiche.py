def main():
    n, d = [int(x) for x in input().split()]
    pedacos = [int(x) for x in input().split()]
    pedacos += pedacos
    p2 = resp = temp = 0
    for i in range(n):     
        while p2 < 2*n and temp < d:
            temp += pedacos[p2]
            p2 += 1
        
        if temp == d:
            resp += 1

        temp -= pedacos[i]
            
    print(resp)

main()
