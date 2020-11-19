def main():
    #leitura
    n = int(input())
    word = input()

    print(solve(n, word))

def solve(n, word):
    divs = divisores(n)

    for d in divs:
        word = word[0:d][::-1] + word[d:]

    return word
    
def divisores(n):
    lista_div = [1]
    temp_div = 2

    while lista_div[-1] < n:
        if not n % temp_div:
            lista_div.append(temp_div)
        temp_div += 1

    return lista_div

main()
