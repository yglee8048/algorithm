# import sys
# sys.stdin = open('input.txt', 'rt')

x, n = map(int, input().split())

# # 내가 처음 푼 풀이
# # 스택 생각이 나지 않아서 정렬을 통해 비교 로직을 구현해보았다.
# arr = []
# str_x = str(x)
# for i in range(len(str_x)):
#     arr.append((int(str_x[i]), i))
#
# res = ""
# s = 0
# while n > 0:
#     tgt = arr[s:s+n+1]
#     if len(tgt) == n:
#         s = len(str_x)
#         break
#     tgt.sort(key=lambda k: (-k[0], k[1]))
#     res += str(tgt[0][0])
#     n -= (tgt[0][1] - s)
#     s = tgt[0][1] + 1
# # 뺄 수가 남지 않았다면 남은 숫자 더해주기
# for y in arr[s:]:
#     res += str(y[0])
# print(res)

# 스택을 이용하여 문제 풀기
# 자신 앞에 자기보다 작은 숫자가 있으면 안 된다.
stack = []
for a in str(x):
    a = int(a)
    while len(stack) > 0 and n > 0 and stack[-1] < a:
        stack.pop()
        n -= 1
    stack.append(a)
# while n > 0:
#     stack.pop()
#     n -= 1
stack = stack[:-n]

# for num in stack:
#     print(num, end="")
print("".join(map(str, stack)))
