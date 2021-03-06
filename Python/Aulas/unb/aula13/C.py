number = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten',
          20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety',
          11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}
def main():
    n = int(input())
    print(solve(n))

def solve(n):
    st = str(n)
    if 0 <= n < 20 or n % 10 == 0:
        return number[n]
    else:
        st = number[int(st[0]) * 10] + '-' + number[int(st[1])]
        return st

main()
