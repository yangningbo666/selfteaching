import math
arr = [int(x) for x in input().split()]
n = arr[0]
m = arr[1]

l = [int(x) for x in input().split()]

def judge(x):
    num = 0
    for i in range(n):
        num += int(l[i]/x)
    return num >= m

def solve():
    left =0
    right = 1000000000
    for q in range(100):
        mid = (left + right) /2
        if judge(mid):
            left = mid
        else:
            right = mid
    result = math.floor(right * 100) /100
    result = ("%2f" % result)
    print(result)

if __name__ == "__main__":
    solve()
    