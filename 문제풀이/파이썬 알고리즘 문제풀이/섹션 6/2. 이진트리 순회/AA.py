import sys
sys.stdin = open('input.txt', 'rt')

n = 7
tree = [1, 2, 3, 4, 5, 6, 7]


# 전위순회
def pre(x):
    if x > n-1:
        return
    # 부모노드 출력
    print(tree[x], end=" ")
    # 좌측노드 탐색
    pre(x*2+1)
    # 우측노드 탐색
    pre(x*2+2)


# 중위순회
def mid(x):
    if x > n-1:
        return
    # 좌측노드 탐색
    mid(x*2+1)
    # 부모노드 출력
    print(tree[x], end=" ")
    # 우측노드 탐색
    mid(x*2+2)


# 후위순회
def post(x):
    if x > n-1:
        return
    # 좌측노드 탐색
    post(x*2+1)
    # 우측노드 탐색
    post(x*2+2)
    # 부모노드 출력
    print(tree[x], end=" ")


pre(0)
print()
mid(0)
print()
post(0)
