# 2212 / 센서

"""
N개 센서, K개 집중국
집중국 길이 최소화

그리디? -> 제일 긴 거리가 수신영역에서 빠져야함

센서 위치 정렬
센서들 간의 거리 계산, 내림차순 정렬 -> 제일 긴 거리를 찾기 위함
가장 큰 거리를 K-1개만큼 제거 -> 수신영역 최소화
"""

import sys
input = sys.stdin.readline

def install(n, sensors, k):
    if k == 1:
        return sensors[-1] - sensors[0]

    dists = []
    for i in range(1, n):
        dists.append(sensors[i] - sensors[i - 1])

    dists.sort()
    return sum(dists[:-k + 1])

def main():
    n = int(input())
    k = int(input())
    sensors = sorted(list(map(int, input().strip().split())))
    print(install(n, sensors, k))

main()