def solution(number, k):
    numbers = list(map(int, number))
    candidates = []
    ans = []
    for i in range(k):
        candidates.append(numbers[i])
    end = k

    while len(candidates) > 0:
        # if already delete or pick all
        if end >= len(numbers):
            for candidate in candidates:
                ans.append(candidate)
            break

        # add one
        candidates.append(numbers[end])
        end += 1

        # find max
        max_v = -1
        max_i = -1
        for i, v in enumerate(candidates):
            # cut edge
            if v == 9:
                max_v = 9
                max_i = i
                break

            if v > max_v:
                max_v = v
                max_i = i
        ans.append(max_v)

        # delete numbers
        candidates = candidates[max_i+1:]

    # remains
    for i in range(end, len(numbers)):
        ans.append(numbers[i])

    # make answer with valid length
    ans_str = ""
    for i in range(len(numbers) - k):
        ans_str += str(ans[i])
    return ans_str
