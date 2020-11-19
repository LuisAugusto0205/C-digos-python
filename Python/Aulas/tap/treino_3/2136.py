def main():
    r = input()
    amigo = None
    lista_s = set()
    lista_n = set()
    
    while r != 'FIM':
        nome, resp = r.split()
        
        if resp == 'YES':
            if amigo is None: amigo = nome
            if len(amigo) < len(nome):
                amigo = nome
            lista_s.add(nome)
        else:
            lista_n.add(nome)

        r = input()

    lista_s = list(lista_s)
    lista_n = list(lista_n)
    lista_s.sort()
    lista_n.sort()
    print('\n'.join(lista_s + lista_n))

    print('\nAmigo do Habay:')
    print(amigo)

main()
