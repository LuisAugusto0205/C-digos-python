def main():
    k = int(input())
    print(solve(k))

def solve(k):
    c = 2
    r = 0
    while r < k:
        num = 9*c + 1
        if perfeito(num):
            r += 1
            imprime(num, c, r)
        c += 1
    return num

def perfeito(num):
    return sum([int(x) for x in str(num)]) == 10

def imprime(num, c, r):
    print('9 x {} + 1 = {:.<20}posição: {}'.format(c, num, r))
