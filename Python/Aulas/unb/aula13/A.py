def main():
    a, b = [int(x) for x in input().split()]
    print(solve(a, b))

def solve(a, b):
    years = 0
    while a <= b:
        a *= 3
        b *= 2
        years += 1
    return years
    
main()
