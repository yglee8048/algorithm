import sys
sys.stdin = open('input.txt', 'rt')


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    l = 0
    r = n-1
    end = 0
    cnt = 0
    ans = ""
    while l <= r:
        if arr[l] > end and arr[r] > end:
            if arr[l] > arr[r]:
                end = arr[r]
                r -= 1
                ans += "R"
            else:
                end = arr[l]
                l += 1
                ans += "L"
            cnt += 1
        elif arr[l] > end:
            end = arr[l]
            l += 1
            ans += "L"
            cnt += 1
        elif arr[r] > end:
            end = arr[r]
            r -= 1
            ans += "R"
            cnt += 1
        else:
            break
    print(cnt)
    print(ans)
