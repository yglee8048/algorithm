from collections import deque
import sys
# sys.stdin = open('input.txt', 'rt')

if __name__ == "__main__":
    n = 7
    arr = [list(map(int, input().split())) for _ in range(n)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visit = [[0]*n for _ in range(n)]
    dq = deque()

    dq.append(((0, 0), 0))
    visit[0][0] = 1
    while dq:
        now = dq.popleft()
        xy = now[0]
        depth = now[1]

        if xy[0] == n-1 and xy[1] == n-1:
            print(depth)
            sys.exit(0)

        for i in range(4):
            nx = xy[0] + dx[i]
            ny = xy[1] + dy[i]
            if any([nx < 0, nx > n-1, ny < 0, ny > n-1]) or any([arr[nx][ny] == 1, visit[nx][ny] == 1]):
                continue
            dq.append(((nx, ny), depth+1))
            visit[nx][ny] = 1
    print(-1)
