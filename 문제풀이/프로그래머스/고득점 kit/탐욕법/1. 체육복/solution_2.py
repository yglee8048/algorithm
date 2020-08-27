def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

    _lost = [l for l in lost if l not in reserve]
    _reserve = [r for r in reserve if r not in lost]
    # _lost = list(set(lost) - set(reserve))
    # _reserve = list(set(reserve) - set(lost))

    p = 0
    q = 0
    cnt = 0
    while p < len(_lost) and q < len(_reserve):
        bf = _lost[p] - 1
        af = _lost[p] + 1

        if bf <= _reserve[q] <= af:
            cnt += 1
            q += 1
            p += 1
        elif _reserve[q] > af:
            p += 1
        else:
            q += 1

    return n - len(_lost) + cnt
