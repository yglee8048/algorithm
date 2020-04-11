import sys
sys.stdin = open('input.txt', 'rt')

n = int(input())
arr = list(map(int, input().split()))

res = [0] * n
idx = []
for i, x in enumerate(arr):
    for j in idx:
        if j <= x:
            x += 1
    res[x] = i + 1
    idx.append(x)
    idx.sort()

for x in res:
    print(x, end=" ")
