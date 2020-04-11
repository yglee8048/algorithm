# import sys
# sys.stdin = open('input.txt', 'rt')

n = int(input())
vol = []
for _ in range(n):
    h, w = map(int, input().split())
    vol.append((h, w))
vol.sort(reverse=True)

# 내가 처음 수행한 완전 탐색에 준하는 풀이
exc = set()
max_ck = 0
for i in range(n):
    wi = vol[i][1]
    if wi < max_ck:
        continue

    max_ck = wi
    for j in range(i+1, n):
        if vol[j][1] < wi:
            exc.add(j)
print(n - len(exc))

# 더 그리디한 좋은 풀이
max_w = 0
cnt = 0
for i in range(n):
    wi = vol[i][1]
    if wi > max_w:
        cnt += 1
        max_w = wi
print(cnt)
