def main():
    pressao = float(input('Qual a pressão?\n'))
    
    if pressao > 1.5:
        print('Desligar')
    else:
        temperatura = float(input('Qual a temperatura?\n'))  
        if temperatura > 300:
            print('Desligar')
        else:
            print('Ligar')

if __name__ == '__main__':
    main()
