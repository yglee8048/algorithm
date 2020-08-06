def solution(m, n, puddles):
    DIV = 1000000007
    # init
    dp = [[0] * (m+1) for _ in range(n+1)]
    for puddle in puddles:
        dp[puddle[1]][puddle[0]] = -1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == j == 1:
                dp[i][j] = 1
                continue
            # puddle check & init
            if dp[i][j] < 0:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % DIV
    return dp[n][m]
