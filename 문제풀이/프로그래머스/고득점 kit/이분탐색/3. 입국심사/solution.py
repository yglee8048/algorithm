def solution(n, times):
    s = 1
    e = max(times) * n

    ans = e
    while s <= e:
        mid = (s+e) // 2
        if n <= sum(map(lambda time: mid // time, times)):
            ans = min(ans, mid)
            e = mid - 1
        else:
            s = mid + 1

    return ans


if __name__ == "__main__":
    print(solution(6, [7, 10]))
