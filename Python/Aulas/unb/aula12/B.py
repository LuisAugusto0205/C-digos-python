def main():
    t, s, x = [int(z) for z in input().split()]
    print(solve(t, s, x))
    
def solve(t, s, x):
    if x < t: return 'NO'
    if x == t or (x >= s and  ((x-t)%s == 0 or (x-t)%s == 1)):
       return 'YES'
    return 'NO'

main()
