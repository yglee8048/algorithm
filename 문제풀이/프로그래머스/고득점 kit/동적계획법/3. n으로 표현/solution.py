def solution(N, number):
    LIMIT = 8  # 최대 8번까지만 탐색한다.

    # cut edge
    if number == N:
        return 1

    # init
    dp = [set() for _ in range(LIMIT+1)]
    dp[1].add(N)

    # i = 사용 횟수
    for i in range(2, (LIMIT + 1)):
        comb = set()
        comb.add(int(str(N) * i))
        # j = 사용 횟수 간의 조합 (ex. 5 = 2 + 3)
        for j in range(1, i):
            for x in dp[j]:
                for y in dp[i-j]:
                    comb.add(x + y)
                    comb.add(x - y)
                    comb.add(x * y)
                    if y != 0:
                        comb.add(x // y)
        dp[i] = comb

        # 찾는 숫자가 존재한다면 현재 사용 횟수를 리턴한다.
        if number in dp[i]:
            return i

    # 8번 모두 찾았는데도 없으면 -1을 리턴한다.
    return -1
