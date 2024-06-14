# 1931 / 회의실 배정
"""
1. 회의를 종료 시간 기준으로 정렬, 종료 시간이 같으면 시작 시간 기준으로 정렬
2. 정렬된 회의를 탐색하며
    선택한 회의의 시작 시간이 현재 시간 이후라면 해당 회의를 시작
"""

import sys
input = sys.stdin.readline

def countMaxMeeting(meetings):
    # 회의를 종료 시간 기준으로 정렬, 종료 시간이 같으면 시작 시간 기준으로 정렬
    meetings.sort(key = lambda x: (x[1], x[0]))

    count = 0
    currentTime = 0

    for meeting in meetings:
        startTime, endTime = meeting
        # 선택한 회의
        if startTime >= currentTime:
            count += 1
            currentTime = endTime

    return count

def main():
    n = int(input())
    meetings = list(tuple(map(int, input().strip().split())) for _ in range(n))
    print(countMaxMeeting(meetings))

main()