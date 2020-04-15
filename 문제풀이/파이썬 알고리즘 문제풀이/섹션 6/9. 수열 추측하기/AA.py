import sys
# sys.stdin = open('input.txt', 'rt')


def dfs(l, psum):
    if l >= n:
        if psum == f:
            for x in res:
                print(x, end=" ")
            sys.exit(0)
    for i in range(n):
        if ck[i] == 0:
            ck[i] = 1
            res[l] = i+1
            dfs(l+1, psum + res[l] * p[l])
            ck[i] = 0


if __name__ == "__main__":
    n, f = map(int, input().split())
    ck = [0] * n
    res = [0] * n
    # pascal 합 = 이항계수
    p = [1] * n
    for i in range(1, n-1):
        p[i] = p[i-1] * (n-i) // i
    dfs(0, 0)
