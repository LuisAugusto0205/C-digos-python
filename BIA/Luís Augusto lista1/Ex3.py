from datetime import datetime
from datetime import timedelta

def main():
    nascimento = datetime.strptime(input('ano de nascimento(DD/MM/AAAA):'),
                                   '%d/%m/%Y')
    atual = datetime.strptime(input('ano atual(DD/MM/AAAA):'),
                              '%d/%m/%Y')

    diasDeVida = atual - nascimento

    print('Você tem {} anos ou {} messes ou {} dias ou {} semanas'.format(diasDeVida.days//365,
                                                                          diasDeVida.days//30,
                                                                          diasDeVida.days,
                                                                          diasDeVida.days//7))

    anos = diasDeVida.days // 365
    messes = (diasDeVida.days % 365)//30
    semanas = ((diasDeVida.days % 365)%30)//7
    dias = ((diasDeVida.days % 365)%30)%7

    print('sua idade é {} anos, {} messes, {} semanas, {} dias'.format(anos, messes,
                                                                       semanas, dias))

main()
