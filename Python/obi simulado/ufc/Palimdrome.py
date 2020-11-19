def main():
    n = int(input())
    cont = 1
    
    while n > 0:
        palavra = input()
        letras = [x for x in palavra]

        print('Teste {}'.format(cont))
        print(solve(letras, n))
        print()
        
        n = int(input())
        cont += 1

def solve(letras, n):
    partes = []
    i = 0
    
    while i < len(letras):
        Maior_p = [letras[i]]
        
        for j in range(i + 1, len(letras)):
            if letras[i] == letras[j]:
                sub_letras = letras[i:j + 1]
                if palindrome(sub_letras) and len(sub_letras) > len(Maior_p):
                    Maior_p = sub_letras[:]    

                
        partes.append(Maior_p[:])
        i += len(Maior_p)

    return len(partes)

def palindrome(letras, maior_p):
    i = 0
    s = len(letras) - 1

    while i <= s:
        if letras[i] != letras[s]:
            return False
        i += 1
        s -= 1
    return True

main()
