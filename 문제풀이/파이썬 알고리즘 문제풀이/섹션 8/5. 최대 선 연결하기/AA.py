import sys
# sys.stdin = open('input.txt', 'rt')

if __name__ == "__main__":
    n = int(input())
    r = list(map(int, input().split()))
    dp = [0] * n

    t_max = 0
    dp[0] = (r[0], 1)
    for i in range(1, n):
        l = r[i]
        p_max = 0
        for j in range(i):
            if dp[j][0] < l:
                if dp[j][1] > p_max:
                    p_max = dp[j][1]

        dp[i] = (l, p_max + 1)
        if dp[i][1] > t_max:
            t_max = dp[i][1]

    print(t_max)
