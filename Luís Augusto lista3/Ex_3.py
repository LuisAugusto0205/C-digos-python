def main():
    num_alunos = int(input('Há quantos alunos na turma?\n'))
    notas = {}
    
    for i in range(num_alunos):
        nome = input('Insira o nome do aluno: ')
        notas[nome] = eval(input('Insira a nota do aluno {}:'.format(nome)))

    media = sum(notas.values())/num_alunos
    print('A média da turma é {:.2f}'.format(media))

    for aluno in notas.keys():
        print('Parabens, {}\n'.format(aluno)*(notas[aluno] > media), end = '')

if __name__ == '__main__':
    main()
