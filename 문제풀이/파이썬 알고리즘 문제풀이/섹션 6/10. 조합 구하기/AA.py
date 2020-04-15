import sys
# sys.stdin = open('input.txt', 'rt')


def dfs(l):
    global cnt
    if l >= m:
        for x in res:
            print(x, end=" ")
        print()
        cnt += 1
        return
    for i in range(res[l-1], n) if l > 0 else range(n):
        if ck[i] == 0:
            ck[i] = 1
            res[l] = i+1
            dfs(l+1)
            ck[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m
    ck = [0] * n
    cnt = 0
    dfs(0)
    print(cnt)
