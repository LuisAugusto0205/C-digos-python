def main():
    n = int(input())
    lista = [int(x) for x in input().split()]
    for num in lista:
        print(solve(num))

def solve(num):
    qnt_d = 1
    dic = {}
    div = 2
    while num > 1:
        if not num % div:
            num //= div
            if div not in dic.keys():
                dic[div] = 1
            else:
                dic[div] += 1
        else:
            div += 1
        if len(dic) > 1:
            break
    for pot in dic.values():
        qnt_d *= (pot+1)
    if qnt_d == 3:
        return 'YES'
    else:
        return 'NO'
main()
