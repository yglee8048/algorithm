import sys
# sys.stdin = open('input.txt', 'rt')

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1, n):
        p_max = 0
        for j in range(i):
            if arr[j] < arr[i]:
                if dp[j] > p_max:
                    p_max = dp[j]
        dp[i] = p_max + 1

    print(max(dp))
