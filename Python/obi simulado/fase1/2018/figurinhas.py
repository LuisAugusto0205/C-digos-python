import bisect

def main():
    n, c, m = [int(x) for x in input().split()]
    carimbadas = [int(x) for x in input().split()]
    compradas = [int(x) for x in input().split()]
    ja_tem = 0
    
    compradas.sort()

    for carimbada in carimbadas:
        i = bisect.bisect_left(compradas, carimbada)
        j = bisect.bisect_right(compradas, carimbada)

        if i != j:
            ja_tem += 1

    print(len(carimbadas) - ja_tem)
        
main()
