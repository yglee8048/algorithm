# import sys
# sys.stdin = open('input.txt', 'rt')

a = list(input())
b = list(input())

a.sort()
b.sort()

if a == b:
    print("YES")
else:
    print("NO")

# 단어 개수가 같으면 됨 = 순회하면서 개수를 센다.
# O(2n) 으로 정렬이 없기 때문에 더 빠르다.
dic = list(dict(), dict())
a = input()
b = input()
for x in a:
    dic[0][x] = dic[0].get(x, 0)
for x in b:
    dic[1][x] = dic[1].get(x, 0)
if dic[0] == dic[1]:
    print("YES")
else:
    print("NO")

# 직접 해시 리스트를 만들고 싶을 때,
# ASCII 를 사용 -> ord(x) = x의 ASCII 넘버를 알려줌
