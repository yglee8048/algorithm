# import sys
# sys.stdin = open('input.txt', 'rt')

n = int(input())
arr = list(map(int, input().split()))

res = [0] * n

# 시간복잡도 n*(n + nlogn) = n^2 log n
# idx = []
# for i, x in enumerate(arr):
#     for j in idx:
#         if j <= x:
#             x += 1
#     res[x] = i + 1
#     idx.append(x)
#     idx.sort()

# 시간복잡도 n^2
for i, val in enumerate(arr):
    for j in range(n):
        if val == 0 and res[j] == 0:
            res[j] = i + 1
            break
        elif res[j] == 0:
            val -= 1

for x in res:
    print(x, end=" ")
