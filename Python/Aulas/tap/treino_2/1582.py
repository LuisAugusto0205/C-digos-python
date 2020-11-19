def mdc(a, b):
    if a < b: a, b = b, a
    if b == 0: return a
    return mdc(b, a%b)

def main():
    while True:
        try:
            resp = ''
            x, y, z = [int(x) for x in input().split()]
            if x > z: z, x = x, z
            if y > z: z, y = y, z
            
            if x**2 + y**2 == z**2:
                if mdc(mdc(x, y), z) == 1:
                    print('tripla pitagorica primitiva')
                else:
                    print('tripla pitagorica')
                
            else:
                print('tripla')
                
        except EOFError:
            break

main()
