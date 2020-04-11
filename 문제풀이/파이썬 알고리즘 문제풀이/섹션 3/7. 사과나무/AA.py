# import sys
# sys.stdin = open('input.txt', 'rt')

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

res, p = 0, 0
cen = n // 2
for i in range(n):
    for j in range(cen-p, cen+p+1):
        res += arr[i][j]
    if i < cen:
        p += 1
    else:
        p -= 1
print(res)
