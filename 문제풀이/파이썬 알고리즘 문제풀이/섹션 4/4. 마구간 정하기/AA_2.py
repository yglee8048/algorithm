import sys
# sys.stdin = open('input.txt', 'rt')


def ck(x):
    global arr

    cnt = 1
    l = arr[0]
    for i in range(1, n):
        if arr[i] - l >= x:
            l = arr[i]
            cnt += 1

    if cnt >= c:
        return True
    else:
        return False


if __name__ == "__main__":
    n, c = map(int, input().split())
    arr = [int(input()) for _ in range(n)]
    arr.sort()

    s = 1
    e = arr[len(arr) - 1] - arr[0]
    ans = 0
    while s <= e:
        mid = (s+e) // 2
        if ck(mid):
            ans = max(ans, mid)
            s = mid + 1
        else:
            e = mid - 1

    print(ans)
