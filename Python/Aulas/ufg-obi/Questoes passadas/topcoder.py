numbers = []
goal = 0
answer = 0

def main():
    global numbers, goal, answer

    #leitura dos dados
    numbers = [int(x) for x in input().split()]
    goal = int(input())

    #inicio da recursão
    combination(0, ['']*len(numbers), 1)

    #saída
    print(answer)
    answer = 0

def combination(pos, comb, condition):
    #base
    if pos < len(comb):
        if comb[pos] != condition: comb[pos] = condition
        else: return
    
    elif pos == len(comb):
        bitwise(comb)
        return

    #recusão
    combination(pos + 1, comb, 1)
    combination(pos, comb, 0)

def bitwise(comb):
    global numbers, goal, answer
    temp_numbers = []
    x = 0
    
    for i in range(len(comb)):
        if comb[i] == 1:#analísa números ativados
            temp_numbers.append(numbers[i])

    for number in temp_numbers: x = x | number   

    if x == goal: answer += 1
