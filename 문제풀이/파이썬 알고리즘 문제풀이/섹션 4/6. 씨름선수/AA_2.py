import sys
sys.stdin = open('input.txt', 'rt')


if __name__ == "__main__":
    n = int(input())
    arr = list(list(map(int, input().split())) for _ in range(n))

    arr.sort(reverse=True)
    p_max = 0
    cnt = n
    for x in arr:
        if x[1] < p_max:
            cnt -= 1
        else:
            p_max = x[1]

    print(cnt)
