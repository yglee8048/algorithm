import sys
# sys.stdin = open('input.txt', 'rt')


if __name__ == "__main__":
    n, w = map(int, input().split())
    dp = [0] * (w+1)
    for _ in range(n):
        jw, jv = map(int, input().split())
        for i in range(jw, w+1):
            dp[i] = max(dp[i - jw] + jv, dp[i])

    print(dp[w])
