import sys
sys.stdin = open('input.txt', 'rt')


def bf(s, e):
    global n, m, arr
    if s >= e:
        return s

    mid = (s+e) // 2
    if arr[mid] == m:
        return mid
    elif arr[mid] > m:
        return bf(s, mid-1)
    else:
        return bf(mid+1, e)


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort()
    print(bf(0, n-1) + 1)
