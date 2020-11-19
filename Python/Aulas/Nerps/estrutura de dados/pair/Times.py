def main():
    n, t = [int(x) for x in input().split()]
    jogadores = []
    
    for _ in range(n):
        jogador = tuple([int(x) if i else x for i, x in
                         enumerate(input().split())][::-1])
        jogadores.append(jogador)

    jogadores.sort(reverse = True)
    
    times = [['Time {}'.format(i + 1)] for i in range(t)]

    #preenchendo os times
    for j in range(n):
        times[j%t].append(jogadores[j][1])

    
    #imprimindo o resultado
    for time in times:
        print(time[0])
        print('\n'.join(sorted(time[1:])))
        print()
    
main()
    
