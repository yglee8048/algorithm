# import sys
# sys.stdin = open('input.txt', 'rt')

n = int(input())
arr = list(map(int, input().split()))

tot, seq = 0, 0
for x in arr:
    if x == 0:
        seq = 0
    else:
        tot += seq + 1
        seq += 1
        # 순서를 바꾸면 tot += seq 도 가능
print(tot)
