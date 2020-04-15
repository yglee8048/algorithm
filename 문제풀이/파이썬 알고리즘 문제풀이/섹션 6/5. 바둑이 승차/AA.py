import sys
# sys.stdin = open('input
# .txt', 'rt')


def dfs(i, ps, ss):
    global ms
    if ps > c:
        return
    if ps + (tot - ss) <= ms:
        return
    if i > n-1:
        if ps > ms:
            ms = ps
        return
    # i는 태우지 않고 진행
    dfs(i+1, ps, ps+w[i])
    # i를 태우고 진행
    dfs(i+1, ps+w[i], ps+w[i])


if __name__ == "__main__":
    c, n = map(int, input().split())
    w = []
    for _ in range(n):
        w.append(int(input()))
    ms = 0
    tot = sum(w)
    dfs(0, 0, 0)
    print(ms)
