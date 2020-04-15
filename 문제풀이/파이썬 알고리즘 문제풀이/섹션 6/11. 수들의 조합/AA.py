import sys
# sys.stdin = open('input.txt', 'rt')


def dfs(l, s, psum):
    global cnt
    if l >= k:
        if psum % m == 0:
            cnt += 1
        return
    for i in range(s, n):
        if ck[i] == 0:
            ck[i] = 1
            dfs(l+1, i+1, psum+arr[i])
            ck[i] = 0


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    m = int(input())
    ck = [0] * n
    cnt = 0
    dfs(0, 0, 0)
    print(cnt)