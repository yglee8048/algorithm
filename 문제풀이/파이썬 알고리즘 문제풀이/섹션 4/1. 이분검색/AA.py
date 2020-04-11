# import sys
# sys.stdin = open('input.txt', 'rt')

n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
# 파이썬 기능 활용하기
# print(arr.index(m) + 1)


# 직접 구현하기
def divFind(s, e):
    cen = (s+e) // 2
    if arr[cen] > m:
        return divFind(s, cen-1)
    elif arr[cen] < m:
        return divFind(cen+1, e)
    else:
        return cen


print(divFind(0, n-1) + 1)
