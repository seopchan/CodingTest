# 19638 / 센티와 마법의 뿅망치

"""
키 / 2 -> floor
min = 1
n 10^5

maxHeight를 때림 -> 최대힙

-> 모든 거인을 target보다 작게 만들 수 있는지?
"""

import heapq
import math
import sys
input = sys.stdin.readline

def main(centiHeight, hammers, giants):
    heapq.heapify(giants)
    success = False
    count = 0

    # 이미 모든 거인의 키가 센티보다 작은 경우
    if -giants[0] < centiHeight:
        print('YES')
        print(count)
        return
    
    for i in range(hammers):
        if giants[0] == -1:
            # 거인 키가 1이면 더이상 진행 불가
            if -giants[0] < centiHeight:
                count = i
                success = True
            break

        heapq.heapreplace(giants, math.ceil(giants[0] / 2))
        if -giants[0] < centiHeight:
            count = i + 1
            success = True
            break
        
    # 성공하거나 centi키가 1이 아닌경우
    if success and -giants[0] < centiHeight:
        print('YES')
        print(count)
    else:
        print('NO')
        print(-giants[0])

N, H, T = map(int, input().split())
giants = [-int(input()) for _ in range(N)]
main(H, T, giants)