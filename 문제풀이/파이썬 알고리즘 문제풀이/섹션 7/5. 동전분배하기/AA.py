import sys
# sys.stdin = open('input.txt', 'rt')


def dfs(l, a, b, c):
    global res
    if l >= n:
        diff = max(a, b, c) - min(a, b, c)
        if a != b and b != c and a != c and diff < res:
            res = diff
        return

    dfs(l+1, a + coin[l], b, c)
    dfs(l+1, a, b + coin[l], c)
    dfs(l+1, a, b, c + coin[l])


if __name__ == "__main__":
    n = int(input())
    coin = []
    for _ in range(n):
        coin.append(int(input()))
    use = [0] * n
    res = 987654321
    dfs(0, 0, 0, 0)
    print(res)
