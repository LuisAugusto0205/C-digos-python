def main():
    amigos = int(input()) + 1
    dedos = sum([int(x) for x in input().split()])
    possib = 0
    
    for i in range(1, 6):
        aux = dedos + i
        if aux % amigos != 1:
            possib += 1
            
    print(possib)

main()
