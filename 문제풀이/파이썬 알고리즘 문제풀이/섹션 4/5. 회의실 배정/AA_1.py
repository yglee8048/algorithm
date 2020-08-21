# import sys
# sys.stdin = open('input.txt', 'rt')

n = int(input())
time_table = []
for _ in range(n):
    s, e = map(int, input().split())
    time_table.append((s, e))

# 정렬
# time_table.sort(key=lambda x: (x[1], x[0]))
time_table = sorted(time_table, key=lambda x: x[1])

# greedy
e = 0
cnt = 0
for schedule in time_table:
    if schedule[0] >= e:
        cnt += 1
        e = schedule[1]
print(cnt)
