# 2075 / N번째 큰 수

# 2차원 배열 r번째 값은 r-1번값 값보다 큼
# 1 <= N <= 1500 -> 225만개
# -10억 e 10억

# 메모리제한 12MB

# - 최댓값을 빼는게 아닌 최솟값만 찾으면서 최솟값을 빼기
# - 최소힙 사용
#     - 힙의 크기를 항상 N으로 유지
#     - 힙에 항상 현재까지 발견한 값 중 가장 큰 N개의 값만 유지
# - 새 값 삽입
#     - 새로운 값을 힙에 삽입할 때, 힙의 크기가 N을 초과하면 가장 작은 값 제거
#     - 힙에 N개의 가장 큰 값만 유지 가능
# - 모든 값 처리 후, 최소 힙의 루트는 N개의 가장 큰 값 중 가장 작은 값
#     - N번째로 큰 수

# 힙의 크기가 최대 N이므로 메모리 최적화 가능!

import heapq
import sys
input = sys.stdin.readline

N = int(input().strip())
hp = [] # 최소힙

for _ in range(N):
    row = list(map(int, input().strip().split()))
    for num in row:
        if len(hp) < N:
            heapq.heappush(hp, num)
        else:
            if num > hp[0]:
                heapq.heappushpop(hp, num)

print(hp[0])