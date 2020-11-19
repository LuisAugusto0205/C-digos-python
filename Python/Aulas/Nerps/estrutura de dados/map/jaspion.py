def main():
    t= int(input())
    for _ in range(t):
        dic = {}
        p, l = [int(x) for x in input().split()]
        
        for i in range(p):
            jap = input()
            br = input()
            dic[jap] = br
            
        for j in range(l):
            resp = ''
            
            for palavra in input().split():
                try:
                    resp += '{} '.format(dic[palavra])
                except KeyError:
                    resp += '{} '.format(palavra)
            
            print(resp[:-1])
        print()
main()
                    
