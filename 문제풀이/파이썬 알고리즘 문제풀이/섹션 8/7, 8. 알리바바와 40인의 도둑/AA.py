import sys
# sys.stdin = open('input.txt', 'rt')
# 다시 한 번 풀어보기!
# 지금 풀이는 별로 좋은 풀이는 아님.
# 점화식의 개념을 적용해 dp스럽게 풀기!


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
    for _ in range(n):
        m.append(list(map(int, input().split())))
    dp = [[999] * n for _ in range(n)]

    dfs(0, 0, m[0][0])
    print(dp[n-1][n-1])
