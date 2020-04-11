# import sys
# sys.stdin = open('input.txt', 'rt')

arr = [x for x in range(21)]
# arr = list(range(21))


def reverse(a, b):
    # a, b = b, a
    # for i in range((a-b+1)//2):
    #     arr[a+i], arr[b-i] = arr[b-i], arr[a+i]
    tmp = arr[a:b+1]
    tmp = tmp[::-1]
    arr[a:b+1] = tmp


for _ in range(10):
    a, b = map(int, input().split())
    reverse(a, b)

for i in range(1, 21):
    print(arr[i], end=" ")
