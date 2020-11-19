def main():
    x = int(input())
    print(solve(x))

def solve(x):
    passos = 0
    for d in range(5, 0, -1):
        passos += x//d
        x %= d
    return passos
main()
