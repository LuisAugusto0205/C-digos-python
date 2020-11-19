def main():
    n = int(input())
    palavra = input()

    print(solve(n, palavra))

def solve(n, palavra):
    restante = [palavra]
    sub_palavras = []
    achou = False
    
    while len(restante) > 0:
        da_vez = restante[0]
        for i in range(len(da_vez), 0, -1):
            for j in range(0, i):
                sub = da_vez[j:i]
                if palindromo(sub):
                    achou = True
                    sub_palavras.append(sub)
                    for x in da_vez.split(sub):
                        if x:
                            restante.append(x)
                    del restante[0]
                    break
            if achou:
                achou = False
                break
    return len(sub_palavras)

def palindromo(palavra):
    return palavra == palavra[::-1]
