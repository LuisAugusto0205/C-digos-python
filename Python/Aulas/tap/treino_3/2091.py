
def main():
    n = int(input())
    while n > 0:
        nums = [int(x) for x in input().split()]
        nums.sort()
        achou = False
        
        while len(nums) > 1:
            x = nums.pop(-1)
            y = nums.pop(-1)

            if x != y:
                print(x)
                achou = True
                break
            
        if achou == False and len(nums) == 1:
            print(nums[0])

        n = int(input())
        

main()
        
