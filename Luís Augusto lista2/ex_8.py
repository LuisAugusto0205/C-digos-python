import random

def main():
    repetidos = []

    for i in range(10):
        davez = random.randint(1, 10)

        while davez in repetidos:
            davez = random.randint(1, 10)

        repetidos.append(davez)
        print(davez)

if __name__ == '__main__':
    main()
    
    
    
        
