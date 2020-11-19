melhor_jogada = 0
def main():
    global melhor_jogada
    
    #leitura dos dados
    t = int(input())
    
    for _ in range(t):
        n = int(input())

        #cria a matriz
        grid = [[int(x) for x in input().split()] for _ in range(n)]

        #cria uma primeira jogada
        jogada = [x for x in range(1, n+1)]
        melhor_jogada = faz_jogada(jogada, grid)

        #analisa todas as jogadas
        permutation(jogada, 0, grid)

        print(melhor_jogada)

        melhor_jogada = 0

def permutation(seq, start, grid):
    global melhor_jogada
    
    for i in range(start, len(seq)):
        seq[i], seq[start] = seq[start], seq[i]
        permutation(seq[:], start + 1, grid)
        
    if start == len(seq):
        pontos = faz_jogada(seq, grid)
        if melhor_jogada > pontos:
            melhor_jogada = pontos
        return

def faz_jogada(jogada, grid):
    pontos = sum([grid[i][j-1] for i, j in enumerate(jogada)])
    return pontos
