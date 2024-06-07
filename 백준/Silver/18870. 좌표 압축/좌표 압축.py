# 18870 / 좌표 압축

from collections import Counter

N = int(input())
arr = list(map(int, input().strip().split()))
setArr = list(set(arr))

sortedArr = sorted(setArr)
ziped = {}
for i, n in enumerate(sortedArr):
    ziped[n]= str(i)

answer = []
for n in arr:
    answer.append(ziped[n])

print(' '.join(answer))