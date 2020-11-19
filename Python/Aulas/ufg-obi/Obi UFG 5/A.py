def main():
    n = int(input())
    cont = 0
    for _ in range(n):
        line = [int(x) for x in input().split()]
        if sum(line) > 1:
           cont += 1
    print(cont)

main()

