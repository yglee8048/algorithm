import sys
# sys.stdin = open('input.txt', 'rt')


def dfs(x, y):
    global cnt
    if x == ex and y == ey:
        cnt += 1
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0<= ny < n and is_visit[nx][ny] == 0 and arr[nx][ny] > arr[x][y]:
            is_visit[nx][ny] = 1
            dfs(nx, ny)
            is_visit[nx][ny] = 0


if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    is_visit = [[0] * n for _ in range(n)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0

    sx, sy, min_h = 0, 0, 987654321
    ex, ey, max_h = 0, 0, -1
    for i in range(n):
        for j in range(n):        
            if arr[i][j] < min_h:
                min_h = arr[i][j]
                sx = i
                sy = j
            if arr[i][j] > max_h:
                max_h = arr[i][j]
                ex = i
                ey = j
    is_visit[sx][sy] = 1
    dfs(sx, sy)
    print(cnt)