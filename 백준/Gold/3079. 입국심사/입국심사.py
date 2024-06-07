# 3079 / 입국심사

import sys
input = sys.stdin.readline

# 1초부터 (최소심사시간 * 인원)까지의 시간을 이분탐색
def binarySearch(times, targetN):
    minTime = 1
    maxTime = min(times) * targetN # 모든 사람이 가장 짧은 시간에 처리 되는 경우

    answer = maxTime

    while minTime <= maxTime:
        mid = (minTime + maxTime) // 2
        # sum (주어진 시간(mid) 동안 각 심사관이 처리할 수 있는 인원)
        peopleProcessed = sum(mid // time for time in times)

        # 주어진 시간(mid) 동안 처리한 사람이 n명 이상이면
        if peopleProcessed >= targetN:
            answer = mid # 현재 시간이 정답 시간
            maxTime = mid - 1 # 시간을 줄여도 가능한지 확인
        else:
            minTime = mid + 1 # 시간을 늘려서 더 많은 사람 처리

    print(answer)

N, M = map(int, input().split())
times = [int(input()) for _ in range(N)]
binarySearch(times, M)