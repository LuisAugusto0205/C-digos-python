def main():
    n = int(input())
    times = [tuple([int(x) for x in input().split()]) for _ in range(n)]
    print(solve(times, n))

def solve(times, n):
    count = 0
    for i in range(n):
        for j in range(n):
            if times[i][0] == times[j][1]:
                count += 1
    return count

main()
