# import sys
# sys.stdin = open('input.txt', 'rt')

n = int(input())
arr = [0] * (n+1)  # arr[n] = 0 : n은 소수
arr[1] = 1  # 1은 소수가 아님
count = 0
for i in range(2, n+1):
    if arr[i] == 0:
        count += 1
        # for j in range(i, n+1, i):
        j = 2
        while i * j <= n:
            arr[i * j] = 1
            j += 1

print(count)
