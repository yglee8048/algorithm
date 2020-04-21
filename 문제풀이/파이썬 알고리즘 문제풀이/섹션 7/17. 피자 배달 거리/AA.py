import sys
# sys.stdin = open('input.txt', 'rt')


def dfs(store_idx, pizza_dis, depth):
    global res
    if depth >= m:
        s = sum(pizza_dis)
        if s < res:
            res = s
        return
    if store_idx >= len(stores):
        return

    # store 폐업
    dfs(store_idx+1, pizza_dis[:], depth)
    # store 유지
    for home_idx, n_dis in enumerate(dis[store_idx]):
        if n_dis < pizza_dis[home_idx]:
            pizza_dis[home_idx] = n_dis
    dfs(store_idx+1, pizza_dis[:], depth+1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    homes = []  # home의 목록
    stores = []  # store의 목록
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                homes.append((i, j))
            elif arr[i][j] == 2:
                stores.append((i, j))

    # dis[store][home] : store에서 home 까지의 거리
    dis = [[0] * len(homes) for _ in range(len(stores))]
    for i, store in enumerate(stores):
        for j, home in enumerate(homes):
            dis[i][j] = abs(store[0] - home[0]) + abs(store[1] - home[1])

    MX = 987654321
    pizza_dis = [MX] * len(homes)  # 각 집의 피자배달거리
    res = MX
    dfs(0, pizza_dis, 0)
    print(res)
