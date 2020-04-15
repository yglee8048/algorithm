import sys
# sys.stdin = open('input.txt', 'rt')


def dfs(i, decode):
    global cnt
    if i >= l:
        print(decode)
        cnt += 1
        return
    if int(code[i]) == 0:
        return

    # 1개 사용
    dfs(i+1, decode + chr(ord('A') + int(code[i]) - 1))
    # 2개 사용
    if i+2 <= l and int(code[i:i+2]) <= 26:
        dfs(i+2, decode + chr(ord('A') + int(code[i:i+2]) - 1))


def ans_dfs(i, p):
    global cnt
    if i == l:
        cnt += 1
        for k in range(p):
            print(chr(ord('A') + int(res[k]) - 1), end="")
        print()

    for j in range(1, 27):
        if code[i] == j:
            res[p] = j
            ans_dfs(i+1, p+1)
        elif j > 9 and code[i] == j // 10 and code[i+1] == j % 10:
            res[p] = j
            ans_dfs(i+2, p+1)


if __name__ == "__main__":
    code = input()
    l = len(code)
    cnt = 0
    dfs(0, "")
    print(cnt)

    code = list(code)
    for i in range(l):
        code[i] = int(code[i])
    code.append(-1)
    res = [0] * l
    cnt = 0
    ans_dfs(0, 0)
    print(cnt)
