from collections import deque
import sys
# sys.stdin = open('input.txt', 'rt')


def bfs(x, y):
    dq = deque()
    dq.append((x, y))
    visit[x][y] = 1
    tot = 0
    while dq:
        xy = dq.popleft()
        tot += 1

        for i in range(4):
            nx = xy[0] + dx[i]
            ny = xy[1] + dy[i]
            if any([nx < 0, nx > n-1, ny < 0, ny > n-1]) or any([arr[nx][ny] == 0, visit[nx][ny] == 1]):
                continue
            dq.append((nx, ny))
            visit[nx][ny] = 1
    return tot


if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, list(input()))) for _ in range(n)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visit = [[0]*n for _ in range(n)]
    dq = deque()

    cnt = 0
    apt = []
    for x in range(n):
        for y in range(n):
            if visit[x][y] == 0 and arr[x][y] == 1:
                cnt += 1
                apt.append(bfs(x, y))
    print(cnt)
    apt.sort()
    for c in apt:
        print(c)
