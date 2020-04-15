import sys
# sys.stdin = open('input.txt', 'rt')


def dfs(now):
    global cnt
    if now == n:
        cnt += 1
        return
    for nxt in g[now]:
        if ck[nxt] == 0:
            ck[nxt] = 1
            dfs(nxt)
            ck[nxt] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    g = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a].append(b)
    ck = [0] * (n+1)
    cnt = 0
    ck[1] = 1
    dfs(1)
    print(cnt)
