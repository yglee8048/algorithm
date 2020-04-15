import sys
# sys.stdin = open('input.txt', 'rt')


def dfs(l, ssum, assum, tsum):
    global res
    if tsum > m:
        return
    if l >= n:
        if ssum > res:
            res = ssum
    if ssum + tot - assum <= res:
        return
    # l번 문제를 푸는 경우
    dfs(l+1, ssum + p[l][0], assum + p[l][0], tsum + p[l][1])
    # l번 문제를 안 푸는 경우
    dfs(l+1, ssum, assum + p[l][0], tsum)


if __name__ == "__main__":
    n, m = map(int, input().split())
    tot = 0
    p = []
    for _ in range(n):
        s, t = map(int, input().split())
        tot += s
        p.append((s, t))
    res = 0
    dfs(0, 0, 0, 0)
    print(res)
