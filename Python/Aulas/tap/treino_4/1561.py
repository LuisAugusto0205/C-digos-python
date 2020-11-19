relogio = [' ____________________________________________',
           '|                                            |',
           '|    ____________________________________    |_',
           '|   |                                    |   |_)',
           '|   |   8         4         2         1  |   |',
           '|   |                                    |   |',
           '',
           '|   |                                    |   |',
           '|   |                                    |   |',
           '',
           '|   |                                    |   |',
           '|   |   32    16    8     4     2     1  |   |_',
           '|   |____________________________________|   |_)',
           '|                                            |',
           '|____________________________________________|']
def main():
    while True:
        try:
            h, m = [int(x) for x in input().split(':')]
            H = ['o' if h & (1 << i) else ' ' for i in range(3, -1, -1)]
            M = ['o' if m & (1 << i) else ' ' for i in range(5, -1, -1)]
            Relogio(H, M)
        except EOFError:
            break

def Relogio(H, M):
    global relogio
    for i in range(15):
        if i == 6:
            print('|   |   ' + (' '*9).join(H) + '  |   |')
        elif i == 9:
            print('|   |   ' + (' '*5).join(M) + '  |   |')
        else:
            print(relogio[i])
    print()

main()
    
