def main():
    n, k = [int(x) for x in input().split()]
    sub_n = [int(x) for x in input().split()]
    if k%2 == 0:
        i, p = k//2, k//2
    else:
        i, p = k//2 + 1, k//2
    sub_impar, sub_par = sorted(sub_n[::2])[:i], sorted(sub_n[1::2])[:p]
    ans = min(sub_impar[-1], sub_par[-1])
    print(ans)

main()
