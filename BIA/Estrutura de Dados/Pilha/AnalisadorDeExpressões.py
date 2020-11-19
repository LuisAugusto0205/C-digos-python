#Autor: Luis Augusto Do Prado Asssunção


#O objetivo deste programa é analisar expressões
#que necessitem de pontuação tais como '()', '[]' e '{}'
#para avaliar se todos os parentes, chaves e concetes abertos foram fechados.
#Para relizar este propósito será utilizada a estruta de dados "Pilha"(FILO).

class Pilha:
    def __init__(self):
        self._i = -1
        self._tamanho = 0
        self._conteudo = []

    def colocar(self, novo_item):
        self._i += 1
        self._tamanho += 1
        
        if self._i == len(self._conteudo):
            self._conteudo.append(None)
        
        self._conteudo[self._i] = novo_item
        
    
    def tirar(self):
        if self._tamanho > 0:
            self._i -= 1
            self._tamanho -= 1

    def topo(self):
        if self._tamanho > 0:
            return self._conteudo[self._i]
        else:
            return None

    @property
    def tamanho(self):
        return self._tamanho







equivalencia = {'(':')', '[':']', '{':'}'}
aberto = equivalencia.keys()
fechado = equivalencia.values()

mensagem_erro = ['\n hummm... Acho que você esqueceu de fechar um{} {}\n antes de fechar um{} {}',
                 '\n cuidado! Você fechou um{} {} sem precisar',
                 '\n Poxa... Você esqueceu de fechar um{} {}',]
                 
                 

def Analise():
    
    grafico()
    executar = 's'
    
    while executar == 's':
        print('+==='*15)
        Expressao = input('\nDigite uma expressão: ')
        achou_erro = False
        
        pilha = Pilha()
        for caractere in Expressao:
            
            if caractere in aberto:
                pilha.colocar(caractere)
            
            elif caractere in fechado:     
                ultimo_aberto = pilha.topo()

                if ultimo_aberto != None and equivalencia[ultimo_aberto] != caractere:
                    
                    print(mensagem_erro[0].format('a' if ultimo_aberto == '{' else '',
                                                ultimo_aberto,
                                               'a' if caractere == '}' else '',
                                                caractere))
                    achou_erro = True
                    break

                if pilha.tamanho == 0:
                    
                    print(mensagem_erro[1].format('a' if caractere == '}' else '',
                                                  caractere))
                    achou_erro = True
                    break
                
                pilha.tirar()

        if not achou_erro and pilha.tamanho > 0:
            print(mensagem_erro[2].format('a' if pilha.topo() == '}' else '',
                                          pilha.topo()))
            achou_erro = True
            
        if not achou_erro:
            print('\n Parabéns! A sua expressão está correta.')

        executar = input('\nEai, vai de novo?(s/n) =D ')
        print()

def grafico():

    print('+' + '-'*58 + '+')
    print('|{:^58}|'.format(''))
    print('|{:^58}|'.format('Analisador de expensões matemáticas'))
    print('|{:^58}|'.format(''))
    print('+'+'-'*58+'+')
    
    print('+' + '-'*27 + '+' + ' '*2 + '+' + '-'*27 + '+')
    print('|{:^27}|  |{:^27}|'.format('', ''))
    print('|{:^27}|  |{:^27}|'.format('Exemplo expressão certa:',
                                      'Exemplo expressão errada:'))
    print('|{:^27}|  |{:^27}|'.format('', ''))

    print('|{:^27}|  |{:^27}|'.format('{[(5 - 2) + 3] x 10}',
                                      '{[(5 - 2)} + (3 x 10)'))

    print('|{:^27}|  |{:^27}|'.format('', ''))
    print('+' + '-'*27 + '+' + ' '*2 + '+' + '-'*27 + '+')

    print('\n Entre com uma expressão matemática\n e o programa dirá se você fechou todos os (, [, {\n')

if __name__ == '__main__':    
    Analise()
    
