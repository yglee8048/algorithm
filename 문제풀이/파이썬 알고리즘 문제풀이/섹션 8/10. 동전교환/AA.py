import sys
# sys.stdin = open('input.txt', 'rt')


if __name__ == "__main__":
    n = int(input())
    kinds = list(map(int, input().split()))
    m = int(input())

    kinds.sort(reverse=True)
    dp = [501] * (m+1)
    dp[0] = 0
    for kind in kinds:
        for i in range(kind, m+1):
            dp[i] = min(dp[i - kind] + 1, dp[i])

    print(dp[m])
