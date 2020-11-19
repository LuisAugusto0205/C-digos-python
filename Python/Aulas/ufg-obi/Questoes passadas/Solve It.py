#p ∗ e**−x + q ∗ sin(x) + r ∗ cos(x) + s ∗ tan(x) + t ∗ x**2 + u = 0
from math import e, cos, sin, tan

def main():
    while True:
        try:
            #leitura dos dados de entrada (termina em EOF)
            coeficientes = [int(x) for x in input().split()]
            #chama as funções
            tem_resposta, crescente = crescente_solucao(*coeficientes) # Verifica se a função tem solução e se ela é crescente
            if not tem_resposta:
                print('No solution')
                continue
            raiz = acha_raiz(*coeficientes, crescente) #encontra a raiz da equação
            print('{:.4f}'.format(raiz)
        except EOFError:
            break

def  crescente_solucao(p, q, r, s, t, u):
    x0 = p * e**0 + q * sin(0) + r * cos(0) + s * tan(0) + t * 0**2 + u # imagem de x=0
    x1 = p * (e**-1) + q * sin(1) + r * cos(1) + s * tan(1) + t * 1**2 + u# imagem de x=1
    if x0 > x1: crescente = False
    else: crescente = True
    if (x0 > 0 and x1 > 0) or (x0 < 0 and x1 < 0): return False, crescente #se x0 e x1 tiverem o mesmo sinal, então não há solução
    else: return True, crescente # #se x0 e x1 tiverem sinais diferentes, então há solução

def acha_raiz(p, q, r, s, t, u, crescente):
    inferior, superior  = 0, 1 #delimitam o valor de x
    meio = (inferior + superior)/2
    y = p * e**(-meio) + q * sin(meio) + r * cos(meio) + s * tan(meio) + t * meio**2 + u
    while abs(y) > 0.0001:
        if (y > 0 and crescente) or (y < 0 and not crescente):
            superior = meio
        elif (y > 0 and not crescente) or (y < 0 and crescente):
            inferior = meio
        meio = (inferior + superior)/2
        y = p * e**(-meio) + q * sin(meio) + r * cos(meio) + s * tan(meio) + t * meio**2 + u
    if y == 0:
        return 0
    return meio

main()
    
    
    
