# import sys
# sys.stdin = open('input.txt', 'rt')

import heapq as hq

l = []
while True:
    n = int(input())
    if n == 0:
        if len(l) == 0:
            print(-1)
        else:
            print(hq.heappop(l))
    elif n == -1:
        break
    else:
        hq.heappush(l, n)
