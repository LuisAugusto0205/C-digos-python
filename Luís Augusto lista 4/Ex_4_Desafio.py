import os

class Agenda:
    def __init__(self):
        self._contatos = {}
        self._tamanho = 0
        self._lerContatos()

    def _lerContatos(self):
        if not os.path.isfile('Agenda.csv'):
            base = open('Agenda.csv', 'w')
            base.close()
        else:
            with open('Agenda.csv', 'r') as agenda:
                line = agenda.readline()
                while line:
                    nome, fone = line.split(';')
                    fone = fone.rstrip('\n')
                    self._contatos[nome] = fone
                    self._tamanho += 1
                    line = agenda.readline()
    
    def _gravarContatos(self, modo, agenda):
        if modo == 'w': self._tamanho = 0
        
        with open('Agenda.csv', modo) as file:
            for pessoa, fone in agenda.items():
                self._contatos[pessoa] = fone
                self._tamanho += 1
                line = pessoa + ';' + fone + '\n'
                file.write(line)

    def _corrigirFone(self, fone):
        fone = ''.join([char for char in fone if char.isdigit()])
        return fone

    def _validarNome(self, nome):
        if len(nome) > 40:
            print('\nNome muito extenso!\n')
            return False
        return True

    def _compararNomes(self, nome1, nome2):
        nome1 = nome1.replace(' ', '').lower()
        nome2 = nome2.replace(' ', '').lower()
        return nome1 == nome2
    
    def adicionar(self, nome, fone):
        fone = self._corrigirFone(fone)
        valido = True
        
        for pessoa in self._contatos.keys():
            if self._compararNomes(nome, pessoa):
                print('\nO nome {} já está registrado'.format(nome))
                print('Tente inserir o sobrenome também\n!')
                valido = False
                break
            
            elif len(nome) > 40:
                valido = self._validarNome(nome)
                break
            
        if len(fone) > 20:
            print('Falha! Número muito extenso.')
            valido = False

        if valido:
            self._gravarContatos('a', {nome: fone})
    
    def busca(self, nome, imprimir = True):
        resultado = {}
        
        for pessoa, fone in self._contatos.items():
            if nome.lower() in pessoa.lower():
                if self._compararNomes(nome, pessoa):
                    self.imprimir({pessoa: fone})
                    return {pessoa: fone}
                resultado[pessoa] = fone

        if imprimir:
            self.imprimir(resultado)
        
        return resultado
    
    def atualizar(self, nome, att_numero = True):
        encontrados = self.busca(nome)
        
        if len(encontrados) == 1:
            for nome in encontrados.keys():
                if not att_numero:
                    novo_fone = input('Novo número: ')
                    if len(novo_fone) < 20:
                        self._contatos[nome] = novo_fone
                        self._gravarContatos('w', self._contatos)
                    else:
                        print('\nTelefone muito extenso!\n')
                    
                else:
                    novo_nome = input('Novo nome: ')
                    if self._validarNome(novo_nome):
                        self._contatos[novo_nome] = self._contatos[nome]
                        del self._contatos[nome]
                        self._gravarContatos('w', self._contatos)
        elif len(encontrados) > 1:
            print('Mais de 1 nome encontrado. seja mais especifico!\n')

    def deletar(self, nome):
        encontrados = self.busca(nome)

        if len(encontrados) == 1:
            del self._contatos[nome]
            self._gravarContatos('w', self._contatos)
        elif len(encontrados) > 1:
            print('Mais de 1 nome encontrado. seja mais especifico!')

    def imprimir(self, agenda = None):
        if agenda is None:
            agenda = self._contatos
        if agenda:
            print('+' + '-'*40 + '+' + '-'*20 + '+')
            print('|{:^40}|{:^20}|'.format('NOMES', 'TELEFONES'))
            print('+' + '-'*40 + '+' + '-'*20 + '+')
        else:
            print('\nNenhum contato encotrado!\n')
        
        for pessoa in sorted(agenda, key = lambda contato: contato.lower()):
            print('|{:^40}|{:^20}|'.format(pessoa, agenda[pessoa]))
            print('+' + '-'*40 + '+' + '-'*20 + '+')
        print()

agenda = Agenda()

def prompt():
    resposta = '0'
    while resposta < '1' or resposta > '5' or not resposta.isdigit():
        print('='*13 + 'AGENDA' + '='*13)
        print('+' + '-'*30 + '+')
        print('|{:<30}|'.format('[1] para ver contatos'))
        print('|{:<30}|'.format('[2] para buscar contato'))
        print('|{:<30}|'.format('[3] para adicionar contato'))
        print('|{:<30}|'.format('[4] para atualizar contato'))
        print('|{:<30}|'.format('[5] para deletar contato'))
        print('+' + '-'*30 + '+')

        resposta = input('\ndigite um número: ')
        print()
        os.system('cls')

    gerenciamento(int(resposta))

def gerenciamento(resposta):
    os.system('cls')
    
    if resposta == 1:
        agenda.imprimir()
              
    elif resposta == 2:
        nome = input('Digite um nome: ')
        agenda.busca(nome)

    elif resposta == 3:
        nome = input('Digite um nome: ')
        fone = input('Digite o número: ')
        agenda.adicionar(nome, fone)
    
    elif resposta == 4:
        objetivo = '0'
        while objetivo < '1' or objetivo > '3' or not objetivo.isdigit():
            print('\n+' + '-'*30 + '+')
            print('|{:<30}|'.format('[1] para atualizar o número'))
            print('|{:<30}|'.format('[2] para atualizar o nome'))
            print('|{:<30}|'.format('[3] Voltar'))
            print('+' + '-'*30 + '+')

            objetivo = input('\ndigite um número: ')
            print()
            os.system('cls')

        objetivo = int(objetivo)
        if objetivo == 1 or objetivo == 2 :
            nome = input('Digite um nome: ')
            agenda.atualizar(nome, objetivo - 1)

    elif resposta == 5:
        nome = input('Digite um nome: ')
        agenda.deletar(nome)
            
    prompt()

if __name__ == '__main__':
    prompt()
    

    
            
    
                    
        
                
    
        
        
