import sys
# sys.stdin = open('input.txt', 'rt')


def dfs(x, y):
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0<= ny < n and is_visit[nx][ny] == 0 and arr[nx][ny] == 1:
            is_visit[nx][ny] = 1
            dfs(nx, ny)


if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    is_visit = [[0] * n for _ in range(n)]
    dx = [1, 0, -1, 0, 1, -1, 1, -1]
    dy = [0, 1, 0, -1, 1, -1, -1, 1]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1 and is_visit[i][j] == 0:
                cnt += 1
                is_visit[i][j] = 1
                dfs(i, j)

    print(cnt)