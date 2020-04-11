# import sys
# sys.stdin = open('input.txt', 'rt')

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


def isMaru(x, y):
    now = arr[x][y]
    # 순회를 더 깔끔하게 하기
    # dx = [1, 0, -1, 0]
    # dy = [0, 1, 0, -1]
    # if all(arr[i][j] > arr[i + dx[k]][j + dy[k]] for k in range(4)):
    # 단, 이 경우에는 선행적으로 가장자리에 0을 추가해둔다.
    # arr.insert(0, [0]*n)
    # arr.append([0]*n)
    # for x in arr:
    #   x.insert(0, 0)
    #   x.append(0)
    if x > 0 and arr[x-1][y] >= now:
        return False
    if y > 0 and arr[x][y-1] >= now:
        return False
    if x < n-1 and arr[x+1][y] >= now:
        return False
    if y < n-1 and arr[x][y+1] >= now:
        return False
    return True


cnt = 0
for i in range(n):
    for j in range(n):
        if isMaru(i, j):
            cnt += 1
print(cnt)
