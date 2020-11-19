def main():
    ano = str(int(input()) + 1)
    while rep(ano):
        ano = str(int(ano) + 1)
    print(ano)

def rep(ano):
    for i in range(4):
        for j in range(i+1, 4):
            if ano[i] == ano[j]:
                return True
    return False

main()
