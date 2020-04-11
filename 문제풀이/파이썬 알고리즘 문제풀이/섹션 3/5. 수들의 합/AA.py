# import sys
# sys.stdin = open('input.txt', 'rt')

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 처음에 구현했던 부분합 알고리즘 > 시간 복잡도 (O^n2)
# sub_sum = [0] * n
# sub_sum[0] = arr[0]
# for i in range(1, n):
#     sub_sum[i] = sub_sum[i-1] + arr[i]

# if sub_sum[n-1] < m:
#     print(0)
# elif sub_sum[n-1] == m:
#     print(1)
# else:
#     cnt = 0
#     for i in range(n):
#         for j in range(i, n):
#             partial_sum = sub_sum[j] - sub_sum[i-1] if i > 0 else sub_sum[j]
#             if partial_sum == m:
#                 cnt += 1
#             elif partial_sum > m:
#                 break
#     print(cnt)

# Greedy 알고리즘
i, j, cnt = 0, 1, 0
sub_sum = arr[i]
# while True:
while j <= n:
    if sub_sum < m:
        if j >= n:
            break
        sub_sum += arr[j]
        j += 1
    elif sub_sum > m:
        sub_sum -= arr[i]
        i += 1
    else:  # equal
        cnt += 1
        sub_sum -= arr[i]
        i += 1
print(cnt)
