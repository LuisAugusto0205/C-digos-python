def crivo(n):
    divisores = [0]*(n + 1)
    R = int(n ** 0.5)

    for i in range(1, R + 1):
        divisores[i * i] += 1
        
        for j in range(i*i + i, n + 1, i):
            divisores[j] += 2

    return divisores

def main():
    div = crivo(2000001)
    resp = [0, 0]
    for i in range(2, 2000001):
        resp.append(resp[i-1])
        if div[div[i]] == 2:
            resp[-1] += 1
    
    while True:
        try:
            n = int(input())

            print(resp[n])
            
        except EOFError:
            break

main()
            
    
