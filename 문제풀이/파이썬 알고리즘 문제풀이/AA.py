import sys
sys.stdin = open('input.txt', 'rt')


def getY(x):
    global arr
    return sum(map(lambda a: a//x, arr))


def bs(s, e):
    global n
    if s >= e:
        return s

    if s == e-1:
        if getY(e) >= n:
            return e
        else:
            return s

    cen = (s+e) // 2
    if getY(cen) >= n:
        return bs(cen, e)
    else:
        return bs(s, cen-1)


if __name__ == "__main__":
    k, n = map(int, input().split())
    arr = [int(input()) for _ in range(k)]

    print(bs(1, max(arr)))
