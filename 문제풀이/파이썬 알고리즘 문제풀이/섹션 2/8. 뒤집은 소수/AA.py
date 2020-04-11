# import sys
# sys.stdin = open('input.txt', 'rt')

n = int(input())
arr = list(map(int, input().split()))
LIM = 100001
is_prime = [0] * (LIM)


def eratos():
    is_prime[1] = 1
    for i in range(2, LIM):
        if is_prime[i] == 0:
            for j in range(2 * i, LIM, i):
                is_prime[j] = 1


def reverse(x):
    rev = ""
    for s in str(x):
        rev = s + rev
    return int(rev)

# def reverse(x):
#     rev = 0
#     while x > 0:
#         rev = rev * 10 + x % 10
#         x = x // 10
#     return rev


def isPrime(x):
    if is_prime[x] == 0:
        return True
    return False


eratos()
for x in arr:
    rev = reverse(x)
    if isPrime(rev):
        print(rev, end=" ")
