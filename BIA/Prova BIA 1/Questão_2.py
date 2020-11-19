from datetime import datetime, timedelta

print('cada item da questão 2 foi resolvido em uma função diferente!')
print('As funções são "itemA()", "itemB()" e "itemC()"\n')
def itemA():
    hoje = datetime.now()
    while True:
        try:
            data = input('Insira a data(dia/mês/ano): ')
            passado = datetime.strptime(data, '%d/%m/%Y')
            delta = hoje - passado
            break
        except:
            print('Formato invalido!')
        
    delta = hoje - passado
    print('A diferença de tempo entre hoje({}) e {} é {} dias'.format(hoje.strftime('%d/%m/%y'),
                                                                 passado.strftime('%d/%m/%y'),
                                                                 abs(delta.days)))
def itemB():
    hoje = datetime.now()
    while True:
        try:
            data = input('Insira a data(dia/mês/ano hora:minuto): ')
            passado = datetime.strptime(data, '%d/%m/%Y %H:%M')
            delta = hoje - passado
            break
        except:
            print('Formato invalido!')
        
    delta = hoje - passado
    st = 'A diferença de tempo entre hoje({}) e {} é {} dias e {} horas, {} minutos, {} segundos'
    print(st.format(hoje.strftime('%d/%m/%y %H:%M'),
                    passado.strftime('%d/%m/%y %H:%M'),
                    abs(delta.days),
                    abs(delta.seconds)//3600,
                    (abs(delta.seconds)%3600)//60,
                    (abs(delta.seconds)%3600)%60))

def itemC():
    while True:
        try:
            data = input('Insira a data(dia/mês/ano): ')
            data = datetime.strptime(data, '%d/%m/%Y')
            break
        except:
            print('Formato invalido!')
            
    print('se quiser subtrair basta colocar número de dias negativos!')
    acrescimo = int(input('Quantos dias quer acrecentar? '))
    data_nova = data + timedelta(days = acrescimo)
    print('A data depois do acrescimo: {}'.format(data_nova.strftime('%d/%m/%y')))
                                                                    
