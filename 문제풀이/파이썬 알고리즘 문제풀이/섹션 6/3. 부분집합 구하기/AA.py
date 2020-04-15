# import sys
# sys.stdin = open('input.txt', 'rt')

n = int(input())
l = list(range(1, n+1))


def dfs(i, now):
    for j in range(i+1, n):
        dfs(j, now + " " + str(j+1))
    print(now)


for i in range(n):
    dfs(i, str(i+1))


# import sys
# #sys.stdin=open("input.txt", "r")
# def DFS(v):
#     if v==n+1:
#         for i in range(1, n+1):
#             if ch[i]==1:
#                 print(i, end=' ')
#         print()
#     else:
#         ch[v]=1
#         DFS(v+1)
#         ch[v]=0
#         DFS(v+1)

# if __name__=="__main__":
#     n=int(input())
#     ch=[0]*(n+1)
#     DFS(1)
