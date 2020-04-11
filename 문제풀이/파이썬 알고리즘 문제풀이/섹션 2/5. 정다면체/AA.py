# import sys
# sys.stdin = open('input.txt', 'rt')

n, m = map(int, input().split())

arr = [0 for _ in range(n+m+1)]
# arr = [0] * (n+m+1)
for i in range(1, n+1):
    for j in range(1, m+1):
        arr[i+j] += 1

max_opp = -1
ans = []
for num, opp in enumerate(arr):
    if opp > max_opp:
        ans = [num]
        max_opp = opp
    elif opp == max_opp:
        ans.append(num)

for x in ans:
    print(x, end=" ")
