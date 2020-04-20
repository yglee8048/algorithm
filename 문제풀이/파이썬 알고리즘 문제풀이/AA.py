import sys
sys.stdin = open('input.txt', 'rt')

def dfs(si, dis, depth):
    global res
    if depth > m:
        s = sum(dis)
        if s < res:
            res = s
            return
    if si >= sl:
        return

    for home in homes:
        home[0]



if __name__ == "__main__":
    n, m = map(int, input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    res = 987654321

    homes = []
    stores = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                homes.append((i, j))
            elif arr[i][j] == 2:
                stores.append((i, j))
    hl = len(homes)
    sl = len(stores)
    dis = [res] * hl
    dfs(0, dis, 0)
    print(res)

