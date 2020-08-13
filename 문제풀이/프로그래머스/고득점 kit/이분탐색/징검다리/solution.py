def ck(arr, n, x):
    cnt = 0
    i = 1
    st = arr[0]
    while i < len(arr):
        if st < x:
            st += arr[i]
            cnt += 1
        else:
            st = arr[i]
        i += 1
    if st < x:
        cnt += 1

    if cnt > n:
        return False
    else:
        return True


def solution(distance, rocks, n):
    rocks += [0, distance]
    rocks.sort()
    arr = [rocks[i] - rocks[i-1] for i in range(1, len(rocks))]

    s = 1
    e = distance
    ans = s
    while s <= e:
        mid = (s+e) // 2
        if ck(arr, n, mid):
            s = mid + 1
            ans = max(ans, mid)
        else:
            e = mid - 1
    return ans
