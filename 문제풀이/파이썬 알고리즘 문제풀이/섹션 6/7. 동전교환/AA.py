import sys
# sys.stdin = open('input.txt', 'rt')


def dfs(psum, cnt):
    global res
    if cnt >= res:
        return
    if psum > money:
        return
    if psum == money:
        if cnt < res:
            res = cnt
        return

    for coin in coins:
        dfs(psum + coin, cnt + 1)


if __name__ == "__main__":
    n = int(input())
    coins = list(map(int, input().split()))
    coins.sort(reverse=True)
    money = int(input())
    res = 987654321
    dfs(0, 0)
    print(res)
