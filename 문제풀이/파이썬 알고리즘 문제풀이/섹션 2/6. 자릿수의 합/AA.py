# import sys
# sys.stdin = open('input.txt', 'rt')

n = int(input())
arr = list(map(int, input().split()))


def digit_sum(x):
    res = 0
    while x >= 1:
        res += x % 10
        x = x // 10
    return res


max_val, res = -1, -1
for x in arr:
    d_sum = digit_sum(x)
    if max_val < d_sum:
        max_val = d_sum
        res = x
print(res)
