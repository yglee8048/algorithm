import sys
# sys.stdin = open('input.txt', 'rt')

INF = 987654

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [[INF]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        arr[i][i] = 0

    for _ in range(m):
        a, b, d = map(int, input().split())
        arr[a][b] = d

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                arr[i][j] = min(arr[i][k] + arr[k][j], arr[i][j])

    for i in range(1, n+1):
        for j in range(1, n+1):
            print(arr[i][j] if arr[i][j] != INF else "M", end=" ")
        print()
