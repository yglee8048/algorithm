import sys
sys.stdin = open('input01.txt', 'rt')

# s < r < p < s
# A == B : A,B 모두 이기는 것
# A != B : A,B 중 이기는 것


def get_win_one(a):
    if a == "S":
        return "R"
    elif a == "R":
        return "P"
    else:
        return "S"


def get_win_two(a, b):
    if get_win_one(a) == b:
        return b
    else:
        return a


if __name__ == "__main__":
    a = list(map(str, input().split()))
    b = list(map(str, input().split()))

    for i in range(len(a)):
        if a[i] == b[i]:
            print(get_win_one(a[i]), end=" ")
        else:
            print(get_win_two(a[i], b[i]), end=" ")
    print()
