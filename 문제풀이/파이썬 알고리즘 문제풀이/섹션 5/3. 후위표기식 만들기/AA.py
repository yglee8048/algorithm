# import sys
# sys.stdin = open('input.txt', 'rt')

# 처음에 생각해내기 어렵다..
# 복습 필수..
cal = input()
stack = []
res = ""
for x in cal:
    if x == "+" or x == "-":
        while len(stack) > 0 and stack[-1] != "(":
            res += stack[-1]
            stack.pop()
        stack.append(x)
    elif x == "*" or x == "/":
        # while stack: == while len(stack)>0:
        while len(stack) > 0 and (stack[-1] == "*" or stack[-1] == "/"):
            res += stack[-1]
            stack.pop()
        stack.append(x)
    elif x == "(":
        stack.append("(")
    elif x == ")":
        while True:
            if stack[-1] == "(":
                stack.pop()
                break
            else:
                res += stack[-1]
                stack.pop()
    else:
        res += x
while len(stack) > 0:
    res += stack[-1]
    stack.pop()
print(res)
