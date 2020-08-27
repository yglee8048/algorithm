def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

    p = 0
    q = 0
    set_lost = []
    set_reserve = []
    while p < len(lost) and q < len(reserve):
        if lost[p] > reserve[q]:
            set_reserve.append(reserve[q])
            q += 1
        elif lost[p] < reserve[q]:
            set_lost.append(lost[p])
            p += 1
        else:
            p += 1
            q += 1
    if p < len(lost):
        for i in range(p, len(lost)):
            set_lost.append(lost[i])
    if q < len(reserve):
        for i in range(q, len(reserve)):
            set_reserve.append(reserve[i])

    cnt_save = 0
    cnt_lost = len(set_lost)
    p = 0
    q = 0
    while p < len(set_lost) and q < len(set_reserve):
        if set_reserve[q] - 1 <= set_lost[p] <= set_reserve[q] + 1:
            p += 1
            q += 1
            cnt_save += 1
        elif set_lost[p] > set_reserve[q] + 1:
            q += 1
        else:
            p += 1

    return n - cnt_lost + cnt_save
