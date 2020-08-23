import sys
sys.stdin = open('input.txt', 'rt')


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    ans = [0] * n
    cnt = [0] * n

    for i, x in enumerate(arr):
        now = x
        while cnt[now] + x > now:
            now = x + cnt[now]

        ans[now] = i + 1
        for j in range(now, n):
            cnt[j] += 1

    for x in ans:
        print(x, end=" ")
