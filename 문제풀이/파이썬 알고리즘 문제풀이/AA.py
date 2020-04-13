import sys
sys.stdin = open('input.txt', 'rt')

must = input()
n = int(input())
sc = []
for _ in range(n):
    sc.append(input())

for i in range(n):
    ck = "" + must
    for x in sc[i]:
        if x in ck:
            if x == ck[0]:
                ck = ck[1:]
            else:
                print("#%d %s" % (i+1, "NO"))
                break
    else:
        if len(ck) > 0:
            print("#%d %s" % (i+1, "NO"))
        else:
            print("#%d %s" % (i+1, "YES"))
