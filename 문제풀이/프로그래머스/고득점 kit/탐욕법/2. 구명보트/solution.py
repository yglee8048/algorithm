def solution(people, limit):

    people.sort()

    answer = 0
    p = 0
    q = len(people) - 1

    while p <= q:
        if people[p] + people[q] <= limit:
            p += 1
            q -= 1
            answer += 1
        else:
            q -= 1
            answer += 1

    return answer
