import sys
sys.stdin = open('input02.txt', 'rt')


# 가려진 개수 = 전체 개수 - 보이는 개수
# z에서 보이는 개수 = x에 대해 y의 개수
# y에서 보이는 개수 = z에 대해 y의 개수
# x에서 보이는 개수 = z에 대해 x의 개수

if __name__ == "__main__":
    n = int(input())
    blocks = []
    for i in range(n):
        blocks.append(list(map(int, input().split())))

    xy_set = set()
    yz_set = set()
    zx_set = set()
    for block in blocks:
        xy_set.add((block[0], block[1]))
        yz_set.add((block[1], block[2]))
        zx_set.add((block[2], block[0]))

    print(n - len(xy_set), n - len(zx_set), n - len(yz_set), sep=" ")
