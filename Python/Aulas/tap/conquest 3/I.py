def main():
    dic = {}

    n = int(input())
    for _ in range(n):
        nome = input()
        try:
            dic[nome] += 1
        except KeyError:
            dic[nome] = 1

    resp = []
    Max = 0
    
    for nome, voto in dic.items():
        if voto > Max:
            Max = voto
            resp = [nome]
            
        elif voto == Max:
            resp.append(nome)

    resp.sort()
    print('\n'.join(resp))

main()
