# import sys
# sys.stdin = open('input.txt', 'rt')

n = int(input())
pre = [input() for _ in range(n)]
poem = [input() for _ in range(n-1)]

for word in pre:
    if word not in poem:
        print(word)
        break

# dictionary 자료구조로 해결하기
p = dict()
for _ in range(n):
    pre = input()
    p[pre] = 1
for _ in range(n):
    poem = input()
    p[poem] = 0
for key, val in p.items():
    if val == 1:
        print(val)
        break
