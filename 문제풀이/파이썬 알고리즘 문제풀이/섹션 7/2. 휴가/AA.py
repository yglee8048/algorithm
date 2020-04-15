import sys
# sys.stdin = open('input.txt', 'rt')


def dfs(day, psum):
    global res
    if day > n:
        return
    if day == n:
        if psum > res:
            res = psum
        return
    if psum + tot[n] - tot[day] <= res:
        return
    dfs(day + sc[day][0], psum + sc[day][1])
    dfs(day + 1, psum)


if __name__ == "__main__":
    n = int(input())
    tot = [0] * (n+1)
    sc = []
    for i in range(n):
        t, p = map(int, input().split())
        sc.append((t, p))
        tot[i+1] = tot[i] + p
    res = 0
    dfs(0, 0)
    print(res)
