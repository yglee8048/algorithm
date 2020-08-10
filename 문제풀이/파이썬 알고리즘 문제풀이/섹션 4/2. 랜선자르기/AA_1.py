# import sys
# sys.stdin = open('input.txt', 'rt')

k, n = map(int, input().split())
arr = []
for _ in range(k):
    arr.append(int(input()))


# x로 잘랐을 때 얻을 수 있는 랜선 개수
def getCnt(x):
    cnt = 0
    for i in range(k):
        cnt += arr[i] // x
    return cnt


rt = max(arr)
lt = 1

res = 0
while lt < rt:
    mid = (lt + rt) // 2
    cnt = getCnt(mid)
    if cnt >= n:
        lt = mid + 1
        if res < mid:
            res = mid
    elif cnt < n:
        rt = mid - 1
print(res)
