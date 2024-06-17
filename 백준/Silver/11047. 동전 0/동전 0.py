# 11047 / 동전 0
"""
동전 A_i는 A_i-1의 배수

즉 큰 동전부터 빼면서 확인한다면 최적해를 구할 수 있음
-> 그리디 알고리즘 적용
"""

import sys
input = sys.stdin.readline

def matchTarget(n, target, coins):
    count = 0
    for coin in coins:
        if target == 0:
            break
        count += target // coin
        target %= coin
    return count

def main():
    n, target = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    coins.reverse() # 값이 큰 동전부터 확인
    print(matchTarget(n, target, coins))

main()