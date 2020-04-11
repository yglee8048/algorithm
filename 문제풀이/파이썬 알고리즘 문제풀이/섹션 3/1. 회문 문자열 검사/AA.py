# import sys
# sys.stdin = open('input.txt', 'rt')


def isCir(s):
    l = len(s)
    s = s.lower()
    for i in range(l // 2):
        if s[i] != s[l-i-1]:
            # s[i] != s[-1-i]
            return False
    return True


n = int(input())
for i in range(n):
    # if s == s[::-1]:
    # s[::-1] : s를 뒤집은 문자열
    if isCir(input()):
        ans = "YES"
    else:
        ans = "NO"
    print("#%d %s" % (i+1, ans))
