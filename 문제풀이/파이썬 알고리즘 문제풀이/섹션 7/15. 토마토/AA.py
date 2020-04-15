from collections import deque
import sys
# sys.stdin = open('input.txt', 'rt')


if __name__ == "__main__":
    m, n = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visit = [[0]*m for _ in range(n)]
    dq = deque()
    depth = 0
    for x in range(n):
        for y in range(m):
            if arr[x][y] == 1:
                dq.append(((x, y), depth))
    while dq:
        now = dq.popleft()
        xy = now[0]
        depth = now[1]

        for i in range(4):
            nx = xy[0] + dx[i]
            ny = xy[1] + dy[i]
            if any([nx < 0, nx > n-1, ny < 0, ny > m-1]) or any([arr[nx][ny] == 1, arr[nx][ny] == -1]):
                continue
            arr[nx][ny] = 1
            dq.append(((nx, ny), depth + 1))

    for x in range(n):
        if 0 in arr[x]:
            print(-1)
            break
    else:
        print(depth)
