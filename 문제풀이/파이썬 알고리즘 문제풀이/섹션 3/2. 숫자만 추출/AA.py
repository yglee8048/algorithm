import re
# import sys
# sys.stdin = open('input.txt', 'rt')


def getDiv(x):
    cnt = 0
    for i in range(1, x//2+1):
        if x % i == 0:
            cnt += 1
    return cnt + 1


s = input()
p = re.compile('[0-9]+')
res = ""
# string.isdecimal() = 숫자인지 확인
for m in p.finditer(s):
    res += m.group()
res = int(res)
print(res)
print(getDiv(res))
