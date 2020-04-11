# import sys
# sys.stdin = open('input.txt', 'rt')

n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
arr = []
max_val = 0
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
    row_sum = sum(row)
    if row_sum > max_val:
        max_val = row_sum

rd_sum = 0
ld_sum = 0
# rd_sum = ld_sum = 0
for i in range(n):
    col_sum = 0
    for j in range(n):
        col_sum += arr[j][i]
        if i == j:
            rd_sum += arr[i][j]
        if i + j == n-1:
            ld_sum += arr[i][j]
    if col_sum > max_val:
        max_val = col_sum
print(max(rd_sum, ld_sum, max_val))
