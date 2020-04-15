import sys
sys.stdin = open('input.txt', 'rt')


def make2nd(x, res):
    q = x // 2
    r = x % 2
    res = str(r) + res
    if q == 0:
        return res
    else:
        return make2nd(q, res)


def dfs(x):
    if x == 0:
        return
    dfs(x//2)
    print(x % 2, end="")


n = int(input())
dfs(n)
print()
print(make2nd(n, ""))
