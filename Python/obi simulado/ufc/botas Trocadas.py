def main():
    n = int(input())
    botas = [input() for _ in range(n)]
    pares = 0
    
    for tam in range(30, 61):
        pares += min(botas.count('{} D'.format(tam)),
                    botas.count('{} E'.format(tam)))
    print(pares)

main()
        
    
    
