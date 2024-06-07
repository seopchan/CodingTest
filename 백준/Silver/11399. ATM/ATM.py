# 11399 / ATM

import sys
input = sys.stdin.readline

N = int(input())
times = list(map(int, input().strip().split()))

totalTime = 0
times.sort()
answer = 0
for t in times:
    totalTime += t
    answer += totalTime
print(answer)