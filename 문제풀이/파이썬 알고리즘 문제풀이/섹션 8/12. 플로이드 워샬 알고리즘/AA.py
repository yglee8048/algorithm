import sys
# sys.stdin = open('input.txt', 'rt')

INF = 987654

if __name__ == "__main__":
    n, m = map(int, input().split())
    dis = [[INF] * n for _ in range(n)]

    for _ in range(m):
        i, j, d = map(int, input().split())
        dis[i-1][j-1] = d

    for i in range(n):
        dis[i][i] = 0

    # i -> k -> j
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

    for i in range(n):
        for j in range(n):
            print("M" if dis[i][j] == INF else dis[i][j], end=" ")
        print()
