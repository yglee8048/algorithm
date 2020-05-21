import sys
# sys.stdin = open('input.txt', 'rt')


def init():
    global n, line

    line = [-1] * (n+1)
    line[0] = 0
    line[1] = 1
    line[2] = 2


def bottom_up():
    global n, line
    init()

    for i in range(3, n+1):
        line[i] = line[i-1] + line[i-2]
    return line[n]


def dfs(x):
    global line
    if line[x] < 0:
        line[x] = dfs(x-1) + dfs(x-2)
    return line[x]


def top_down():
    global n, line
    init()

    return dfs(n)


if __name__ == "__main__":
    n = int(input())
    line = [-1] * (n+1)

    # print(bottom_up())
    print(top_down())
