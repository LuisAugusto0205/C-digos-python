Exemplo = [['Cachorro velho não aprende truque novo', 'Meu sapo jururu'],
           ['Super Mario Brother'                   , 'Show no rio'    ]]

entrada = 'rio'

def buscar(valores, entrada):
    resposta = []
    
    for i in range(len(valores)):
        for j in range(len(valores[0])):
            if entrada in valores[i][j]:
                resposta.append(valores[i][j])
    
    return resposta

print(buscar(Exemplo, entrada))
