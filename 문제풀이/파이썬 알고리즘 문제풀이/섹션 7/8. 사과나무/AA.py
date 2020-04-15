from collections import deque
import sys
# sys.stdin = open('input.txt', 'rt')

if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visit = [[0] * n for _ in range(n)]

    dq = deque()
    res = 0
    visit[n//2][n//2] = 1
    dq.append(((n//2, n//2), 0))
    while dq:
        now = dq.popleft()
        xy = now[0]
        depth = now[1]
        res += arr[xy[0]][xy[1]]

        if depth >= n//2:
            continue

        for i in range(4):
            nxt_x = xy[0] + dx[i]
            nxt_y = xy[1] + dy[i]
            if visit[nxt_x][nxt_y] == 0:
                visit[nxt_x][nxt_y] = 1
                dq.append(((nxt_x, nxt_y), depth+1))
    print(res)
