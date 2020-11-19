def main():
    n = int(input())
    
    for _ in range(n):
        x = int(input())
        i = 2
        primo = True
         
        while i * i <= x:
            if x % i == 0:
                primo = False
                break
            i += 1
            
        if primo: print('Prime')
        else: print('Not Prime')
    
main()
