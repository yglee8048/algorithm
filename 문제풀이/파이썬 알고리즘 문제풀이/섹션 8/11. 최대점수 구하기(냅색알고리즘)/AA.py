import sys
# sys.stdin = open('input.txt', 'rt')


if __name__ == "__main__":
    n, m = map(int, input().split())
    problems = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(n):
        for j in range(problems[i][1], m+1):
            dp[i+1][j] = max(dp[i][j],
                             dp[i][j-problems[i][1]] + problems[i][0])

    print(dp[n][m])
