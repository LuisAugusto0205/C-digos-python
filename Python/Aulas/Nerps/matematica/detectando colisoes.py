def main():
    r1 = [int(x) for x in input().split()]
    coord1 = [(r1[0], r1[1]), (r1[0], r1[3]),(r1[2], r1[1]), (r1[2], r1[3])]
    r2 = [int(x) for x in input().split()]
    coord2 = [(r2[0], r2[1]), (r2[0], r2[3]),(r2[2], r2[1]), (r2[2], r2[3])]
    '''try:
        a = input()
    except:
        pass'''

    for x, y in coord1:
        if r2[1] <= y <= r2[3] and r2[0] <= x <= r2[2]:
            print(1)
            return

    for x, y in coord2:
        if r1[1] <= y <= r1[3] and r1[0] <= x <= r1[2]:
            print(1)
            return

    if r1[2] <= r2[2] and r1[0] >= r2[0] and r1[3] >= r2[3] and r1[1] <= r2[1]:
        print(1)
        return
    if r2[2] <= r1[2] and r2[0] >= r1[0] and r2[3] >= r1[3] and r2[1] <= r1[1]:
        print(1)
        return
    print(0)

main()
        
