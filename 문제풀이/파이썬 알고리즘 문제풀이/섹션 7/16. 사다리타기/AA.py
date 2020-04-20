import sys
# sys.stdin = open('input.txt', 'rt')

def dfs(x, y):
    if y == 0:
        print(x)
        sys.exit(0)
    
    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and arr[ny][nx] == 1 and is_visit[ny][nx] == 0:
            is_visit[ny][nx] = 1
            dfs(nx, ny)



if __name__ == "__main__":
    n = 10
    arr = [list(map(int, input().split())) for _ in range(n)]

    dx = [1, -1, 0]
    dy = [0, 0, -1]
    is_visit = [[0] * n for _ in range(n)]

    for i in range(n):
        if arr[n-1][i] == 2:
            is_visit[n-1][i] = 1
            dfs(i, n-1)
            break