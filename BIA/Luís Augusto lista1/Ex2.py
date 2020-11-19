def main():
    salario = int(input('Informe o salário: '))
    acresimo =  1 + (int(input('Informe o acréscimo(em %): '))/100)
    print('O novo salário será: R${:.2f}'.format(salario * acresimo))
main()
