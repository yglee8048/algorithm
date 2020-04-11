# import sys
# sys.stdin = open('input.txt', 'rt')

arr = [list(map(int, input().split())) for _ in range(7)]

cnt = 0
for i in range(7):
    for j in range(3):
        # 가로
        rw = arr[i][j:5+j]
        if rw == rw[::-1]:
            cnt += 1
        co = []
        # 세로
        for h in range(j, 5+j):
            co.append(arr[h][i])
        if co == co[::-1]:
            cnt += 1
print(cnt)
