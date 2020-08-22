import sys
sys.stdin = open('input.txt', 'rt')


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    l, r = 0, n-1
    cnt = 0

    while l <= r:
        if arr[l] + arr[r] <= m:
            l += 1
            r -= 1
        else:
            r -= 1
        cnt += 1

    print(cnt)
