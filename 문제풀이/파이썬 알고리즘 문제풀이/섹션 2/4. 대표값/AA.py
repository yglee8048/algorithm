# import sys
# sys.stdin = open('input.txt', 'rt')

n = int(input())
score = list(map(int, input().split()))

avg = round(sum(score) / n) # 사실 round(sum(score) / n + 0.5) 로 해야 정확함

# min_diff, tgt_score, tgt_num = -1, -1, -1
# for i in range(n):
#   diff = avg - score[i] if avg > score[i] else score[i] - avg

#   if min_diff < 0 or min_diff > diff:
#     min_diff = diff
#     num = i+1
#     tgt_score = score[i]
#   elif min_diff == diff:
#     if tgt_score < score[i]:
#       num = i+1
#       tgt_score = score[i]
# print("%d %d" %(avg, num))

min_diff, tgt_score, tgt_num = 987654321, -1, 987654321
for num, value in enumerate(score):
  diff = abs(avg - value)
  if min_diff > diff:
    min_diff = diff
    tgt_num = num + 1
    tgt_score = value
  elif min_diff == diff:
    if tgt_score < value:
      tgt_num = num + 1
      tgt_score = value
print(avg, tgt_num)
