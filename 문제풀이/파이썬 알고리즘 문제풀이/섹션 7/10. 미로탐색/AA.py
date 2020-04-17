import sys
# sys.stdin = open('input.txt', 'rt')

def dfs(x, y):
    global cnt
    if x == n-1 and y == n-1:
        cnt += 1
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0<= ny < n and is_visit[nx][ny] == 0 and arr[nx][ny] == 0:
            is_visit[nx][ny] = 1
            dfs(nx, ny)
            is_visit[nx][ny] = 0




if __name__ == "__main__":
    n = 7
    arr = [list(map(int, input().split())) for _ in range(n)]
    is_visit = [[0] * n for _ in range(n)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0

    is_visit[0][0] = 1
    dfs(0,0)
    print(cnt)