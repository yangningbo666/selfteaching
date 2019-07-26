n = int(input())
arr = [int(x) for x in input().split()]
stack = []
arr.append(0)
result = 0
i = 0
presum = []
tempsum = 0
while  i < len(arr):
    if not stack or arr[i] >= stack[-1]:
        presum.append(tempsum)
        tempsum = 0
        stack.append(arr[i])
        i += 1
    else:
        temp = stack.pop(-1)
        tempsum += (temp + presum.pop())
        result = max(tempsum * temp, result)
print(result)