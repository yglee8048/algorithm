def solution(triangle):
    # init
    dp = [[0] * (i+1) for i in range(len(triangle)+1)]
    dp[0][0] = triangle[0][0]

    my_triangle = triangle[:]
    my_triangle.append([0] * (len(triangle)+1))

    # i = 층수 (0부터 시작)
    for i in range(len(triangle)):
        # i층의 j번째
        for j in range(i+1):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j] + my_triangle[i+1][j])
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + my_triangle[i+1][j+1])

    return max(dp[len(triangle)])
