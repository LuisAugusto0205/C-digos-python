def main():
    n, m, a = [int(x) for x in input().split()]
    p = m*n
    qnt_m = m//a + (m%a != 0)*1
    qnt_n = n//a + (n%a != 0)*1
    qnt_g = qnt_m * qnt_n
    print(qnt_g)

main()
