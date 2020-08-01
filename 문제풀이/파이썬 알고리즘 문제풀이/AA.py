import sys
sys.stdin = open('input.txt', 'rt')


def dfs(x, y, w):
    global n, dp
    dx = [1, 0]
    dy = [0, 1]

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < n and ny < n:
            if dp[nx][ny] > w + m[nx][ny]:
                dp[nx][ny] = w + m[nx][ny]
                dfs(nx, ny, dp[nx][ny])


if __name__ == "__main__":
    n = int(input())
    m = []
    m.append(list(map(int, input().split())) for _ in range(n))
    dp = [[999] * n for _ in range(n)]

    dfs(0, 0, m[0][0])
    print(dp[n-1][n-1])
