# 11286 / 절댓값 힙

# 배열에 정수 x 넣기
# 배열에서 절댓값이 가장 작은 값 출력, 배열에서 제거

# 1. 최소 힙 -> heapq
# 2. 각 숫자별 부호의 개수를 저장
# 3. 1을 힙에서 빼면서 -> 부호 개수 dict에서 -,+ 순으로 개수 확인

# 0일 때 배열에서 빼기, 배열이 비어있으면 0출력

import heapq
from sys import stdin

def task(hq, dic, sign):
    dic[minVal][sign] -= 1
    return heapq.heappop(hq) if sign else -heapq.heappop(hq)

N = int(stdin.readline())
hq = []
dic = {} # -개수, +개수

for _ in range(N):
    num = int(stdin.readline())

    if num == 0:
        pass
        answer = 0
        if hq:
            minVal = hq[0]
            sign = 0 if dic[minVal][0] > 0 else 1
            answer = task(hq, dic, sign)
        
        print(answer)

    else:
        absNum = abs(num)
        if absNum not in dic:
            dic[absNum] = [0, 0]

        sign = 0 if num < 0 else 1
        dic[absNum][sign] += 1
            
        heapq.heappush(hq, absNum)