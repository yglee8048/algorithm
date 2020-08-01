import sys
# sys.stdin = open('input.txt', 'rt')

if __name__ == "__main__":
    n = int(input())
    blocks = []
    for i in range(n):
        blocks.append(list(map(int, input().split())))

    blocks.sort(reverse=True)

    dp = [0] * n
    t_max = blocks[0][1]
    dp[0] = blocks[0][1]
    for i in range(1, n):
        w = blocks[i][2]
        p_max = 0
        for j in range(i):
            if blocks[j][2] > w:
                if dp[j] > p_max:
                    p_max = dp[j]
        dp[i] = p_max + blocks[i][1]
        if dp[i] > t_max:
            t_max = dp[i]

    print(t_max)
