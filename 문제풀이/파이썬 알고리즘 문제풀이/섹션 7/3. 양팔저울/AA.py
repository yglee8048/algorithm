import sys
# sys.stdin = open('input.txt', 'rt')


def dfs(l, ws):
    if l < k:
        dfs(l+1, ws + w[l])
        dfs(l+1, ws - w[l])
        dfs(l+1, ws)
    if ws > 0:
        can[ws] = 1  # set으로 넣고 len(set) 도 가능


if __name__ == "__main__":
    k = int(input())
    w = list(map(int, input().split()))
    s = sum(w)

    # dfs
    can = [0] * (s+1)
    dfs(0, 0)

    # count
    cnt = 0
    for i in range(1, s+1):
        if can[i] == 0:
            cnt += 1
    print(cnt)
