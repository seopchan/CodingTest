# 2512 / 예산

"""
상한액

1. 모든 요청이 가능하면 그대로 배정
2. 넘치면 상한액 산정

예산을 구해야하는데 예산이 n~10억
-> 합이 전체 예산 이하 | 합이 전체 예산 초과
-> 이분탐색
"""

import sys
input = sys.stdin.readline
MAX_VAL = 1_000_000_000

def getTotalMoneyWithLimit(moneys, limit):
    totalMoney = 0
    for money in moneys:
            totalMoney += min(money, limit)
    return totalMoney

def binarySearch(moneys, maxMoney):
    left, right = 1, maxMoney
    limitMoney = 0

    while left <= right:
        mid = (left + right) // 2
        # 상한가 초과 예산을 상한가로 맞춘 합
        totalMoney = getTotalMoneyWithLimit(moneys, mid)
        
        if totalMoney <= maxMoney: # 총액보다 작으면 상한가 늘려서 확인
             limitMoney = mid
             left = mid + 1
        elif totalMoney > maxMoney: # 총액보다 크면 상한가 줄여서 확인
             right = mid - 1

    return limitMoney

def main():
    n = int(input())
    moneys = list(map(int, input().strip().split()))
    maxMoney = int(input())

    if sum(moneys) <= maxMoney:
        print(max(moneys))
    else:
        print(binarySearch(moneys, maxMoney))

main()