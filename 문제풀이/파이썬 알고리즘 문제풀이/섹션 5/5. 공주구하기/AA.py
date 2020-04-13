from collections import deque
# import sys
# sys.stdin = open('input.txt', 'rt')

# queue 대신 dequeue 를 사용한다.

n, k = map(int, input().split())
q = deque(list(range(1, n+1)))
while q:
    for _ in range(k-1):
        q.append(q.popleft())
    q.popleft()
    if len(q) == 1:
        print(q.popleft())
