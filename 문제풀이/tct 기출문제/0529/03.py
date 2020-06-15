import sys
sys.stdin = open('input03.txt', 'rt')


# 프로의 경기를 최대로 하기 위해서는
# 프로를 아마추어가 더 많은 쪽에 넣어야 한다.


def binary_search(s, e, depth):
    global summ
    print(s, e, depth, sep=" ")
    if s == e:
        return s

    left, right = 0, 0
    l, r = s, e
    for i in range(depth):
        cen = int((l+r)/2)
        if l == 0:
            left += summ[i][cen]
        else:
            left += summ[i][cen] - summ[i][l-1]
        right += summ[i][r] - summ[i][cen]

        l = int(l/2)
        r = int(r/2)

    print("left :", left)
    print("right :", right)
    if left >= right:
        binary_search(s, int((s+e)/2), depth-1)
    else:
        binary_search(int((s+e)/2)+1, e, depth-1)


def make_ton(depth):
    global ton, n
    x = int(n/(2**depth))
    print(x)
    for i in range(x):
        p_ton = []
        if ton[depth-1][2*i] + ton[depth-1][2*i+1] == 0:
            p_ton.append(0)
        else:
            p_ton.append(1)
    ton.append(p_ton)
    print(ton)


def get_sum():
    global ton
    summ = []
    for p_ton in ton:
        p_summ = [p_ton[0]]
        print(p_summ)
        for i in range(1, len(p_ton)):
            p_summ.append(p_ton[i] + p_summ[i-1])
            print(p_summ)
        summ.append(p_summ)
    return summ


if __name__ == "__main__":
    n = int(input())
    players = list(map(int, input().split()))

    # 초기 토너먼트 대진/결과 만들기
    ton = [players]
    depth = 1
    while len(ton[depth-1]) > 1:
        print(ton, depth)
        make_ton(depth)
        depth += 1
    
    # 개수를 빠르게 구하기 위한 합 배열
    summ = get_sum()
    
    # 이진탐색
    ans = binary_search(0, n-1, len(ton) - 1)
    players[ans] = 1
    
    # 최종 토너먼트 대진/결과 만들기
    ton = [players]
    depth = 1
    while len(ton[depth-1]) > 1:
        make_ton(depth)
        depth += 1
    
    res = 0
    for p_ton in ton:
        for p in p_ton:
            res += p
    print(res)


