#Autor: Luis Augusto Do Prado Asssunção

# Esta programa é um sistema de gerenciamento de fila no banco
# utilizando a estrutura de dados 'Fila'(FIFO)

class Fila():
    def __init__(self):
        self._conteudo = []
        self._primeiro = 0
        self._ultimo = -1

    def colocar(self, novo_item):
        self._ultimo += 1
        if self._ultimo == len(self._conteudo):
            self._conteudo.append(None)

        self._conteudo[self._ultimo] = novo_item
        
    def tirar(self):
        if self._ultimo > -1 and self._primeiro <= self._ultimo:
            self._primeiro += 1
        else:
            return None
        
    def primeiro(self):
        if self._ultimo > -1 and self._primeiro <= self._ultimo:
            return self._conteudo[self._primeiro]
        else:
            return None

    @property
    def tamanho(self):
        if self._primeiro <= self._ultimo:
            return self._ultimo - self._primeiro + 1
        else:
            return 0
        

def Fila_banco():
    grafico('Fachada')
    fila = Fila()
    
    operacao = ''
    while operacao != '3':
        grafico('Menu')
        operacao = input('\n Digite o número da operação desejada: ')

        if operacao == '1':
            nome = input('\nInsira o nome da Pessoa: ')
            fila.colocar(nome)
            grafico('1', nome)

        elif operacao == '2':
            if fila.tamanho > 0:
                nome = fila.primeiro()
                fila.tirar()
                grafico('2', nome)
                
            else:
                grafico('Vazio')

        elif operacao == '3':
            grafico('3')

        else:
            grafico('Invalido')
        
def grafico(tipo, nome = ''):
    if tipo == 'Fachada':
        print('*'*60)
        print('*{:^58}*'.format(''))
        print('*{:^58}*'.format('Genciamento da fila do Banco'))
        print('*{:^58}*'.format(''))
        print('*'*60 + '\n')
        
    elif tipo == 'Menu':
        print('{:^60}'.format('+' + '='*38 + '+'))
        print('{:^60}'.format('|{:^38}|'.format('Menu')))
        print('{:^60}'.format('|{:^38}|'.format('')))
        print('{:^60}'.format('|{:<38}|'.format('[1] Colocar uma Pessoa na fila')))
        print('{:^60}'.format('|{:<38}|'.format('[2] Chamar o próximo cliente')))
        print('{:^60}'.format('|{:<38}|'.format('[3] Fechar o sistema')))
        print('{:^60}'.format('|{:^38}|'.format('')))
        print('{:^60}'.format('+' + '='*38 + '+'))
    

    elif tipo == '1':
        print('\n{:^60}\n'.format(nome + ' entrou na fila!'))
        print('\n' + '='*60 + '\n')

    elif tipo == '2':
        print('\n{:^60}\n'.format('Auto-falante: Por favor, ' + nome + ' Compareça ao Caixa!'))
        print('\n' + '='*60 + '\n')

    elif tipo == '3':
        print('\n{:^60}\n'.format('Fechando o Sistema...'))

    elif tipo == 'Vazio':
        print('\n{:^60}\n'.format('Não há ninguém na fila!'))
        print('\n' + '='*60 + '\n')

    elif tipo == 'Invalido':
        print('\nNúmero invalido! Tente Novamente.')
        print('Os números validos estão no Menu!\n')

if __name__ == '__main__':
    Fila_banco()


