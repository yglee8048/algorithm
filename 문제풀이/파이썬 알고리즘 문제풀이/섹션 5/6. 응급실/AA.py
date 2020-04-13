from collections import deque
# import sys
# sys.stdin = open('input.txt', 'rt')

n, m = map(int, input().split())
wlist = list(map(int, input().split()))

# wq = deque()
# for i, x in enumerate(wlist):
#     wq.append((i, x))
wq = deque([(i, x) for i, x in enumerate(wlist)])
wlist.sort(reverse=True)
mq = deque(wlist)


def solve():
    cnt = 0
    while mq:
        now_max = mq.popleft()
        while wq:
            now = wq.popleft()
            if now[1] != now_max:
                wq.append(now)
            else:
                cnt = cnt + 1
                if now[0] == m:
                    print(cnt)
                    return
                else:
                    break


solve()
