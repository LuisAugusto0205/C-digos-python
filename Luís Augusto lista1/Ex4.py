def main():
    SacoKg = int(input('O saco de ração tem quantos quilogramas? '))
    gato = int(input('Quanto cada gato consome por dia? '))
    sobrou = SacoKg - 10 * gato
    print('{} Kg sobra no quinto dia'.format(sobrou) * (sobrou > 0) +
          '0 Kg sobra no quinto dia'*(sobrou <= 0))

main()
