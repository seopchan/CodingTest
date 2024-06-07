# 2110 / 공유기 설치

# N개의 집
# 공유기를 c개 설치할 때, 가장 인접한 공유기의 간격이 최대가 되어야 함
# 0 - c개 설치 가능 | c개 설치 불가능 - 최대 간격
# mid를 변경하며 모든 공유기를 설치할 수 있는 간격의 최댓값 찾기

import sys
input = sys.stdin.readline

def isInstallAble(n, houses, distance, routers):
    # 첫 집에 공유기를 설치하고 시작
    installed = 1
    lastInstalled = houses[0]

    # 모든 집을 돌면서 정해진 간격 이상으로 설치가 가능하면 설치
    # 주어진 공유기를 다 설치했으면 True
    # 주어긴 간격으로 다 설치할 수 없으면 False
    for i in range(1, n):
        if houses[i] - lastInstalled >= distance:
            installed += 1
            lastInstalled = houses[i]
            if installed >= routers:
                return True
    return False

def binarySearch(n, houses, routers):
    left = 0
    right = houses[-1] - houses[0]
    distance = right + 1

    while left <= right:
        mid = left + (right - left) // 2
        
        # mid거리만큼 간격을 두었을 때 모두 설치 가능하면
        if isInstallAble(n, houses, mid, routers):
            distance = mid # 최대 간격 갱신
            left = mid + 1 # 더 큰 간격으로 시도
        else:
            right = mid - 1 # 설치할 수 없으면, 더 작은 간격으로 시도

    print(distance)

N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]
houses.sort()

binarySearch(N, houses, C)