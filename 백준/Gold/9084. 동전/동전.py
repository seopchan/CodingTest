# 9084 / 동전

"""
동전의 종류, 주어진 금액

1. dp[w]는 금액 w를 만들기 위한 모든 방법의 수 저장
2. dp[0] = 1, 0원을 만드는 방법은 1가지
3. 각 동전에 대해, 해당 동전을 사용해 금액 w를 만드는 방법의 수 갱신
    dp[w] += dp[w - coin] -> 현재 금액 w에서 coin을 사용한 새로운 방법의 수 추가
4. dp[target]이 금액을 만드는 모든 방법의 수
"""
import sys
input = sys.stdin.readline

def coinCombinations(coins, target):
    dp = [0] * (target + 1)
    dp[0] = 1

    for coin in coins:
        for w in range(coin, target + 1):
            dp[w] += dp[w - coin]

    print(dp[target])

def main():
    case = int(input())
    for _ in range(case):
        n = int(input())
        coins = map(int, input().strip().split())
        target = int(input())
        coinCombinations(coins, target)

main()