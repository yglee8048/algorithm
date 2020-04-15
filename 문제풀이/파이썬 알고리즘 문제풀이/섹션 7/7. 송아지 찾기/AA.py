from collections import deque
import sys
# sys.stdin = open('input.txt', 'rt')

if __name__ == "__main__":
    s, e = map(int, input().split())
    move = [5, 1, -1]
    visit = [0] * 10000

    dq = deque()
    dq.append((s, 0))
    while dq:
        now = dq.popleft()
        if now[0] < 1 or now[0] >= 10000 or visit[now[0]] == 1:
            continue
        if now[0] == e:
            print(now[1])
            sys.exit(0)

        visit[now[0]] = 1
        for i in range(3):
            dq.append((now[0] + move[i], now[1] + 1))
