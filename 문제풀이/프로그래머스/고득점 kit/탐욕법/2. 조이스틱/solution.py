def countUpDown(x):
    return min(ord("Z") - ord(x) + 1, ord(x) - ord("A"))


def solution(name):
    answer = 0

    # A를 제외한 문자열을 통해 개수를 세고, 지나쳐야하는 A의 갯수를 더해준다.
    t_cnt = name.count("A")  # 전체 A의 갯수
    _name = name.replace("A", "")  # A를 제외한 문자열

    # A가 있는 경우
    if t_cnt > 0:
        seq = False  # A가 연속으로 이어지는지 여부
        max_cnt = 0  # 연속적인 A 갯수 중 최댓값
        end = -1  # 연속적인 A의 등장이 종료된 시점
        cnt = 0  # 연속적인 A의 갯수

        # 최대 연속 A를 찾는다.
        for i in range(len(name)):
            if name[i] == "A":
                seq = True
                cnt += 1  # 연속적인 A의 갯수
            else:
                if seq:
                    if cnt > max_cnt:
                        max_cnt = cnt
                        end = i
                    seq = False
                    cnt = 0
        # A로 끝난 경우
        if seq:
            if cnt > max_cnt:
                max_cnt = cnt
                end = len(name)

        # 찾은 최대 연속 A를 통해 판단
        # 연속 A를 건너가는 것보다 다시 돌아가는 게 빠르다면
        if max_cnt > (end - max_cnt) - 1:  # 연속 A 건너가기 > 다시 돌아가기
            # answer += 돌아가는 거리 + 연속 A를 제외한 A의 수(연속 A는 건너가지 않으므로)
            answer += ((end - max_cnt) - 1 + (t_cnt - max_cnt))
        else:
            answer += t_cnt  # 그냥 A를 모두 건너간다

    # A를 제외한 문자열로 개수를 센다.
    for x in _name:
        answer += countUpDown(x) + 1
    answer -= 1  # 최초의 경우 이동할 필요 없으므로 이미 더해준 이동거리 1을 다시 제외한다.

    return answer
