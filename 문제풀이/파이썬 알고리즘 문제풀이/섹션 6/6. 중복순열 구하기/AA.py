import sys
# sys.stdin = open('input.txt', 'rt')


def dfs(l):
    global cnt
    if len(l) >= m:
        cnt += 1
        for x in l:
            print(x, end=" ")
        print()
        return

    for i in range(1, n+1):
        l.append(i)
        dfs(l)
        l.pop()


# append/pop 없이
def ans_dfs(l):
    global cnt
    if l >= m:
        cnt += 1
        for x in res:
            print(x, end=" ")
        print()
        return
    for i in range(1, n+1):
        res[l] = i
        ans_dfs(l+1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    cnt = 0
    dfs([])
    print(cnt)

    cnt = 0
    res = [0] * m
    ans_dfs(0)
    print(cnt)
