# import sys
# sys.stdin = open('input.txt', 'rt')

from collections import deque

n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

l, r = 0, n-1
cnt = 0
while l <= r:
    if arr[l] + arr[r] <= m:
        l += 1
        r -= 1
        cnt += 1
    else:
        cnt += 1
        r -= 1
print(cnt)

# deque 를 사용하면 효율적으로(재정렬 없이) 앞, 뒤에서 pop 할 수 있다.
# dq = deque(arr)
# cnt = 0
# while dq:
#     if len(dq) == 1:
#         cnt += 1
#         break
#     if dq[0] + dq[-1] > m:
#         cnt += 1
#         dq.pop()
#     else:
#         cnt += 1
#         dq.pop()
#         dq.popleft()
# print(cnt)
