import sys
# sys.stdin = open('input.txt', 'rt')


def dfs(l, sum):
    global cnt
    if sum > t:
        return
    if sum == t:
        cnt += 1
        return
    if l >= k:
        return
    coin = coins[l]
    for x in range(coin[1]+1):
        dfs(l+1, sum + coin[0] * x)


if __name__ == "__main__":
    t = int(input())
    k = int(input())
    coins = [list(map(int, input().split())) for _ in range(k)]
    cnt = 0
    dfs(0, 0)
    print(cnt)
