def main():
    t = int(input())
    for _ in range(t):
        seq = [char for char in input()]
        resposta = set()
        permutation(seq, 0, resposta)
        aux = []
        for permuta in resposta:
            aux.append(permuta)
        print(' '.join(aux))
            
def permutation(seq, start, resposta):
    for i in range(start, len(seq)):
        seq[i], seq[start] = seq[start], seq[i]
        permutation(seq, start + 1, resposta)
        seq[i], seq[start] = seq[start], seq[i]
        
    if start == len(seq):
        resposta.add(''.join(seq))
        #print(''.join(seq))
        return

main()
