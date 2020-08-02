import sys
sys.stdin = open('input.txt', 'rt')


def dfs(x, y):
    if dp[x][y] != 0:
        return dp[x][y]
    if x == 0 and y == 0:
        dp[0][0] = arr[0][0]
    elif x == 0:
        dp[x][y] = dfs(x, y-1) + arr[x][y]
    elif y == 0:
        dp[x][y] = dfs(x-1, y) + arr[x][y]
    else:
        dp[x][y] = min(dfs(x, y-1), dfs(x-1, y)) + arr[x][y]
    return dp[x][y]


if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * n for _ in range(n)]

    print(dfs(n-1, n-1))
