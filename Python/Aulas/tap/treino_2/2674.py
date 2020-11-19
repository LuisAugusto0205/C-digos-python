primos = [2, 3, 5, 7]

def primo(n):
    if n < 2: return False
    i = 2
    
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    
    return True

def main():
    global primos
    
    while True:
        try:
            n = int(input())
            
            if primo(n):
                Super = True
                while n > 0:
                    num = n%10
                    n //= 10
                    
                    if num not in primos:
                        Super = False
                
                if Super:
                    print('Super')
                else:
                    print('Primo')
            
            else:
                print('Nada')
                
        except EOFError:
            break

main()
