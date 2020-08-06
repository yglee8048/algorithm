def solution(money):
    # 마지막 집을 반드시 턴다면
    dp = [0] * len(money)
    for i in range(len(money)):
        if i == 0 or i == len(money)-2:
            dp[i] = 0
        else:
            dp[i] = max(dp[i-1], (dp[i-2] + money[i]) if i > 1 else money[i])
    max_with_end = max(dp)

    # 마지막 집을 반드시 안 턴다면
    dp = [0] * len(money)
    dp[0] = money[0]
    for i in range(1, len(money) - 1):
        dp[i] = max(dp[i-1], (dp[i-2] + money[i]) if i > 1 else money[i])
    max_without_end = max(dp)

    return max(max_with_end, max_without_end)
