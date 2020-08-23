# import sys
# sys.stdin = open('input.txt', 'rt')

n = int(input())
arr = list(map(int, input().split()))
l, r = 0, n-1
res = ""
e = 0

while l <= r:
    if arr[l] <= arr[r]:
        if arr[l] > e:
            res += "L"
            e = arr[l]
            l += 1
        else:
            if arr[r] > e:
                res += "R"
                e = arr[r]
                r -= 1
            else:
                break
    else:
        if arr[r] > e:
            res += "R"
            e = arr[r]
            r -= 1
        else:
            if arr[l] > e:
                res += "L"
                e = arr[l]
                l += 1
            else:
                break
print(len(res))
print(res)
