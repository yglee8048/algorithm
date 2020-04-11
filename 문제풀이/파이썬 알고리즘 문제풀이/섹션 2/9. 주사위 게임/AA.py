# import sys
# sys.stdin = open('input.txt', 'rt')

n = int(input())
max_val = 0
for _ in range(n):
    dice = list(map(int, input().split()))
    # a, b, c = map(int, input().split())
    if dice[0] == dice[1] and dice[1] == dice[2]:
        p = 10000 + dice[0] * 1000
    elif dice[0] == dice[1] or dice[0] == dice[2]:
        p = 1000 + dice[0] * 100
    elif dice[1] == dice[2]:
        p = 1000 + dice[1] * 100
    else:
        p = max(dice) * 100
    if p > max_val:
        max_val = p
print(max_val)
