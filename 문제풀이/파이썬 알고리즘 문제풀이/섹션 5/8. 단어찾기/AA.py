# import sys
# sys.stdin = open('input.txt', 'rt')

n = int(input())
pre = [input() for _ in range(n)]
poem = [input() for _ in range(n-1)]

for word in pre:
    if word not in poem:
        print(word)
        break
