# import sys
# sys.stdin = open('input.txt', 'rt')

n = int(input())
score = list(map(int, input().split()))

avg = round(float(sum(score)) / float(len(score)))
min_diff, tgt_score, tgt_num = -1, -1, -1
for i in range(n):
  diff = avg - score[i] if avg > score[i] else score[i] - avg

  if min_diff < 0 or min_diff > diff:
    min_diff = diff
    num = i+1
    tgt_score = score[i]
  elif min_diff == diff:
    if tgt_score < score[i]:
      num = i+1
      tgt_score = score[i]
print("%d %d" %(avg, num))
