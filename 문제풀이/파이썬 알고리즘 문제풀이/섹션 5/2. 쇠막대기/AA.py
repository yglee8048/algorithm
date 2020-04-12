# import sys
# sys.stdin = open('input.txt', 'rt')

s = input()
stack = []
res = 0
for i in range(len(s)):
    if s[i] == '(':
        stack.append('(')
    else:
        stack.pop()
        if s[i-1] == '(':
            res += len(stack)
        else:            
            res += 1
print(res)
