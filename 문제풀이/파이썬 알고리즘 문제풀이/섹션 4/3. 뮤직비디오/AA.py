# import sys
# sys.stdin = open('input.txt', 'rt')

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 처음 풀었던 방법 : 완전탐색에 준하는 그리디 = 시간 초과
# sub_sum = [0] * n
# sub_sum[0] = arr[0]
# for i in range(1, n):
#     sub_sum[i] = sub_sum[i-1] + arr[i]
# div = list(range(1, m))
# div.append(n)


# def getMax():
#     max_i = -1
#     max_val = -1
#     for i in range(m):
#         if i == 0:
#             now_sum = sub_sum[div[i]-1]
#         else:
#             now_sum = sub_sum[div[i]-1] - sub_sum[div[i-1]-1]

#         if now_sum > max_val:
#             max_i = i
#             max_val = now_sum
#     return max_i, max_val


# min_storage = 987654321
# while 1:
#     max_i, max_val = getMax()
#     if max_val < min_storage:
#         min_storage = max_val

#     if max_i == 0:
#         break
#     div[max_i - 1] += 1
# print(min_storage)


# 결정 알고리즘 풀기
# 정답의 범위를 특정할 수 있는가?
# >> 정답을 정해두고 이분탐색으로 범위를 좁혀가며 최적해를 찾는다.
lt = min(arr)
rt = sum(arr)
min_storage = 987654321
while lt <= rt:
    mid = (lt + rt) // 2
    cnt = 1
    a_sum = 0
    for i in range(n):
        a_sum += arr[i]
        if a_sum > mid:
            a_sum = arr[i]
            cnt += 1
    if cnt <= m:
        if mid < min_storage:
            min_storage = mid
        rt = mid - 1
    else:
        lt = mid + 1
print(min_storage)
