import sys
# sys.stdin = open('input.txt', 'rt')


def dfs(i, psum):
    if i > n-1:
        if psum == ans:
            print("YES")
            sys.exit(0)
        return
    dfs(i+1, psum)
    if psum + i <= ans:
        dfs(i+1, psum + l[i])


if __name__ == "__main__":
    n = int(input())
    l = list(map(int, input().split()))
    lsum = sum(l)
    if lsum % 2 != 0:
        print("NO")
        sys.exit(0)
    ans = lsum // 2
    dfs(0, 0)
