# import sys
# sys.stdin = open('input.txt', 'rt')

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


def rotat(rw, dr, ds):
    ds = ds % n
    rw -= 1
    tmp = [0] * n
    if dr == 0:
        tmp[0:n-ds] = arr[rw][ds:n]
        tmp[n-ds:n] = arr[rw][0:ds]
    else:
        tmp[0:ds] = arr[rw][n-ds:n]
        tmp[ds:n] = arr[rw][0:n-ds]
    arr[rw] = tmp


def getSum():
    res, p = 0, 0
    cen = n // 2
    for i in range(n):
        res += sum(arr[i][p:n-p])
        if i < cen:
            p += 1
        else:
            p -= 1
    return res


m = int(input())
for _ in range(m):
    rw, dr, ds = map(int, input().split())
    rotat(rw, dr, ds)
print(getSum())
