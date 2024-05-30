# 점수 중 최댓값 M
# 모든 점수를 점수 / M * 100

import sys

N = sys.stdin.readline()
scores = list(map(int, sys.stdin.readline().split()))
M = max(scores)

sumVal = 0
for score in scores:
    sumVal += score / M * 100

avg = sumVal / len(scores)
print(avg)