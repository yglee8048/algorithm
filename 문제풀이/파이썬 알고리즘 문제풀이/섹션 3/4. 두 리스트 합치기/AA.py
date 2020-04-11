# import sys
# sys.stdin = open('input.txt', 'rt')

n = int(input())
arr_n = list(map(int, input().split()))
m = int(input())
arr_m = list(map(int, input().split()))

p, q = 0, 0
res = []
# while 조건에 반복 조건을 적어주는 것이 가시성이 더 나음
while 1:
    if p >= n:
        for i in range(q, m):
            res.append(arr_m[i])
        break
    if q >= m:
        for i in range(p, n):
            res.append(arr_n[i])
        break
    if arr_n[p] < arr_m[q]:
        res.append(arr_n[p])
        p += 1
    else:
        res.append(arr_m[q])
        q += 1

for x in res:
    print(x, end=" ")
