# import sys
# sys.stdin = open('input.txt', 'rt')

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

arr.sort()
p, q = 0, 0
for _ in range(m):
    arr[n-1] -= 1
    arr[0] += 1

    # 풀이에서는 그냥 arr.sort() 했음..
    i = 0
    while i < n:
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            i += 1
        else:
            break
    i = 0
    while i < n:
        if arr[n-i-1] < arr[n-i-2]:
            arr[n-i-1], arr[n-i-2] = arr[n-i-2], arr[n-i-1]
            i += 1
        else:
            break
print(arr[n-1] - arr[0])
