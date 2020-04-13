# import sys
# sys.stdin = open('input.txt', 'rt')

cal = input()
stack = []
for x in cal:
    if x.isdecimal():
        stack.append(x)
    else:
        if x == "+":
            n = int(stack[-2]) + int(stack[-1])
            stack = stack[:-2]
            stack.append(n)
        elif x == "-":
            n = int(stack[-2]) - int(stack[-1])
            stack = stack[:-2]
            stack.append(n)
        elif x == "*":
            n = int(stack[-2]) * int(stack[-1])
            stack = stack[:-2]
            stack.append(n)
        else:
            n = int(stack[-2]) / int(stack[-1])
            stack = stack[:-2]
            stack.append(n)
print(stack[-1])
