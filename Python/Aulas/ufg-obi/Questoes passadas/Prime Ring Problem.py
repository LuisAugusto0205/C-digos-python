primos = []

def crivo(n):
    global primos
    
    naturais = [[0, False], [1, False]] + [[x, True] for x in range(2, n+1)]
    
    for i in range(2, n+1):
        if not naturais[i][1]: continue
        else:
            primos.append(naturais[i][0])
            for j in range(i, n+1, i):
                naturais[j][1] = False
            
def main():
    crivo(32)
    caso = 1
    while True:
        try:
            n = int(input())
            impares = [x for x in range(3, n, 2)]
            pares = [x for x in range(2, n+1, 2)]

            gravados = []
            respostas = []

            permutation(impares, 0, 'impar', gravados, respostas)
            permutation(pares, 0, 'par', gravados, respostas)

            respostas = respostas[:len(respostas)//2][::-1] + respostas[len(respostas)//2:]

            print('Case {}'.format(caso))
            for resposta in respostas:
                for i in range(n):
                    if i == n - 1: print(resposta[i])
                    else: print(resposta[i], end = ' ')
            print()
            caso += 1
        except EOFError:
            primo = []
            break

def valida_sequencia(seq):
    global primos
    
    for i in range(len(seq)):
        if seq[i-1] + seq[i] not in primos:
            return False
    return True

def permutation(seq, start, paridade, gravados, respostas):
    for i in range(start, len(seq)):
        seq[i], seq[start] = seq[start], seq[i]
        permutation(seq[:], start + 1, paridade, gravados, respostas)

    if start == len(seq):
        if paridade == 'impar':
            gravados.append([1] + seq)
        else:
            for seq_impar in gravados:
                da_vez = []
                for n in range(len(seq)):
                    da_vez.append(seq_impar[n])
                    da_vez.append(seq[n])
                if valida_sequencia(da_vez): respostas.append(da_vez)
        return

main()
