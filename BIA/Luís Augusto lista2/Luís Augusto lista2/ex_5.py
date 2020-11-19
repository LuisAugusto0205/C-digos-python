def main():
    print('digite os nomes dos alunos\nao terminar aperte "Enter" sem nenhum nome')
    alunos = []
    davez = input()
    
    while davez:
        alunos.append(davez)
        davez = input()
        
    for i in range(len(alunos) - 1):
        for j in range(i + 1, len(alunos)):
            print('{} e {}'.format(alunos[i], alunos[j]))

if __name__ == '__main__':
    main()
            

