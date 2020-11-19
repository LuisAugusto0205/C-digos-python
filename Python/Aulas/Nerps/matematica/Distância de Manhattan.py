def main():
    x_m, y_m, x_r, y_r = [int(x) for x in input().split()]
    resposta = abs(x_m - x_r) + abs(y_m - y_r)
    print(resposta)
main()
