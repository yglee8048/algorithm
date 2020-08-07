import sys
# sys.stdin = open('input.txt', 'rt')

INF = 987654

if __name__ == "__main__":
    n = int(input())
    dy = [[INF] * n for _ in range(n)]
    while True:
        a, b = map(int, input().split())
        dy[a-1][b-1] = 1
        dy[b-1][a-1] = 1
        if a == b == -1:
            break

    for i in range(n):
        dy[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dy[i][j] = min(dy[i][j], dy[i][k] + dy[k][j])

    score = [0] * n
    for i in range(n):
        score[i] = max(dy[i])

    min_score = min(score)
    candidates = []
    for i in range(n):
        if score[i] == min_score:
            candidates.append(i+1)

    print(min_score, len(candidates), sep=" ")
    for candidate in candidates:
        print(candidate, end=" ")
