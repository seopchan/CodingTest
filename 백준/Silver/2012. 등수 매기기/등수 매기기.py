# 2012 / 등수 매기기

"""
정렬된 예상 등수로 실제 등수를 정하면
예상 등수와 실제 등수 차이 최소화 가능

1. 예상 등수를 오름차순으로 정렬 -> 불만도를 최소화
2. 실제 등수와 비교 -> 총 불만도 계산
"""

import sys
input = sys.stdin.readline

def calcTotalComplain(n, expectedRanks):
    # 예상 등수를 오름차순으로 정렬
    expectedRanks.sort()
    # 실제 등수 1~N
    actualRanks = list(range(1, n + 1))
    # 총 불만도 계산
    totalComplain = sum(abs(expectedRanks[i] - actualRanks[i]) for i in range(n))

    return totalComplain

def main(): 
    n = int(input())
    expectedRanks = [int(input()) for i in range(n)]
    print(calcTotalComplain(n, expectedRanks))

main()
    