def e_primo(x):
    if x == 1: return 'N'
    i = 2
    while i*i <= x:
        if not x % i: return 'S'
        i += 1
    return 'N'

def main():
    print(e_primo(int(input())))

main()
