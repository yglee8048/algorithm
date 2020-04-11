# import sys
# sys.stdin = open('input.txt', 'rt')

n = 9
arr = [list(map(int, input().split())) for _ in range(n)]
st = list(range(1, 10))


# 내가 처음 푼 방법 = sort = O(n log n)
def isOk():
    for i in range(n):
        tmp = arr[i][:]
        tmp.sort()
        if tmp != st:
            return "NO"

        tmp = []
        for j in range(n):
            tmp.append(arr[j][i])
        tmp.sort()
        if tmp != st:
            return "NO"

    for i in range(3):
        for j in range(3):
            tmp = []
            for h in range(i*3, i*3+3):
                tmp += arr[h][j*3:j*3+3]
            tmp.sort()
            if tmp != st:
                return "NO"
    return "YES"


# O(n) 체크하기
# check array를 만들어서 0으로 초기화 > 숫자가 나오면 1로 바꿈
# 1이 중복되면 오류
def isOkBetter():
    for i in range(9):
        ck_x = [0] * 10
        ck_y = [0] * 10
        for j in range(9):
            if ck_x[arr[i][j]] == 1 or ck_y[arr[j][i]] == 1:
                return "NO"
            else:
                ck_x[arr[i][j]] = 1
                ck_y[arr[j][i]] = 1
    for i in range(3):
        for j in range(3):
            ck = [0] * 10
            for h in range(i*3, i*3+3):
                for w in range(j*3, j*3+3):
                    if ck[arr[h][w]] == 1:
                        return "NO"
                    else:
                        ck[arr[h][w]] = 1
    return "YES"


# print(isOk())
print(isOkBetter())
