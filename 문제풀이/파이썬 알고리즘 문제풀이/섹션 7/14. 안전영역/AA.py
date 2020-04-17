from collections import deque
import sys
# sys.stdin = open('input.txt', 'rt')

def bfs(x, y, rain):
    dq = deque()
    dq.append((x,y))
    is_visit[x][y] = 1

    while dq:
        xy = dq.popleft()
        
        for i in range(4):
            nx = xy[0] + dx[i]
            ny = xy[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < n and is_visit[nx][ny] == 0 and arr[nx][ny] > rain:
                dq.append((nx, ny))
                is_visit[nx][ny] = 1
            

if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    max_h = 0
    for i in range(n):
        h = max(arr[i])
        if h > max_h:
            max_h = h
    
    res = 0
    for rain in range(1, max_h+1):
        is_visit = [[0] * n for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                if arr[i][j] > rain and is_visit[i][j] == 0:
                    cnt += 1
                    bfs(i, j, rain)
        if cnt > res:
            res = cnt

    print(res)