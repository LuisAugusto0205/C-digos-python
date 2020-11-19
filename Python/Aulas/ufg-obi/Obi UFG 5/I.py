def main():
    palavra = input()
    print(solve(palavra))

def solve(palavra):
    tamanho_sub = 0
    
    for i in range(len(palavra)):
        sub_palavra = palavra[i:]
        if sub_palavra == sub_palavra[::-1]: #se for palidrome
            tamanho_sub = len(sub_palavra)
            break

    restante_palavra = palavra[:len(palavra) - tamanho_sub]

    palindrome = palavra + restante_palavra[::-1]

    return palindrome

main()
