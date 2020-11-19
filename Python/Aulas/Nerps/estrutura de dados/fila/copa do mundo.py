from queue import Queue
def main():
    fila = Queue()
    time1 = ord('a')
    time2 = ord('b')
    for i in range(15):
        if i < 8:
            jogo = [int(x) for x in input().split()]
            gols = max(jogo)
            fila.put(chr(time1) if jogo.index(gols) == 0 else chr(time2))
            time1 += 2
            time2 += 2
        else:
            time1 = fila.get()
            time2 = fila.get()
            jogo = [int(x) for x in input().split()]
            gols = max(jogo)
            fila.put(time1 if jogo.index(gols) == 0 else time2)
    print(fila.get().upper())

main()
        
            
