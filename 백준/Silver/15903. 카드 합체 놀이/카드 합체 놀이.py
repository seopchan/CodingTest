# 15903 / 카드 합체 놀이

# 1. x + y
# 2. x, y = x + y

# 최소힙 사용

import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
hp = []

arr = map(int, input().strip().split())
for num in arr:
    heapq.heappush(hp, num)

for _ in range(M):
    # 최소값 2개 꺼내기
    x = heapq.heappop(hp)
    y = heapq.heappop(hp)
    # 합 2개 추가하기
    heapq.heappush(hp, x + y)
    heapq.heappush(hp, x + y)

print(sum(hp))