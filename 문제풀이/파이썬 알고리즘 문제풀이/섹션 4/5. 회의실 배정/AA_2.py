import sys
sys.stdin = open('input.txt', 'rt')


if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort(key=lambda x: x[1])

    cnt = 0
    e = 0
    for x in arr:
        if x[0] >= e:
            e = x[1]
            cnt += 1

    print(cnt)
