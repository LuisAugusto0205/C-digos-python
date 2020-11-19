def main():
    palavra = input()
    print(solve(palavra))
    
def solve(palavra):
    n_letras = 0
    i = 0
    correcao = 0
    resposta = palavra
    while i < len(palavra):
        if palavra[i] == ' ':
            i += 1
            continue
        else:
            n_letras += 1
            
        if n_letras and n_letras % 2 == 1:
            resposta = resposta[:i - correcao] + resposta[i + 1 - correcao:]
            correcao += 1
        i += 1
    return resposta
            
main()
