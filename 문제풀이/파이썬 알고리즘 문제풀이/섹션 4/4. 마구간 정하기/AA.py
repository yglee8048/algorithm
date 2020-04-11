# import sys
# sys.stdin = open('input.txt', 'rt')

n, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()
dis = []
for i in range(1, n):
    dis.append(arr[i] - arr[i-1])
# 마굿간 사이 거리를 미리 구해두지 않고,
# 순회 중에 (현재 좌표 - 이전 좌표) 와 같은 형태로도 구할 수 있다.

lt = 1
rt = arr[n-1]
max_val = 0
while lt <= rt:
    min_dis = (lt + rt) // 2

    sub_sum = 0
    cnt = 1
    for i in range(n-1):
        sub_sum += dis[i]
        if sub_sum >= min_dis:
            sub_sum = 0
            cnt += 1

    if cnt < c:
        rt = min_dis - 1
    else:
        if min_dis > max_val:
            max_val = min_dis
        lt = min_dis + 1
print(max_val)
