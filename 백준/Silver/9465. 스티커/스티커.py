# 9465 / 스티커

"""
점수의 합 최대 DP

1. O  OX  OXO  
   X  XO  XOX ...

2. X  XO  XOX
   O  OX  OXO ...
"""

import sys
input = sys.stdin.readline

def getMaxVal(n, stickers):
    if n == 1:
        return max(stickers[0][0], stickers[1][0])

    # dp 배열을 0으로 초기화
    dp = [[0] * n for _ in range(2)]

    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]

    dp[0][1] = stickers[0][1] + dp[1][0]
    dp[1][1] = stickers[1][1] + dp[0][0]

    for i in range(2, n):
        dp[0][i] = stickers[0][i] + max(dp[1][i - 1], dp[1][i - 2])
        dp[1][i] = stickers[1][i] + max(dp[0][i - 1], dp[0][i - 2])

    return max(dp[0][n-1], dp[1][n-1])

def main():
    case = int(input())
    for _ in range(case):
        n = int(input())
        stickers = [list(map(int, input().strip().split())) for _ in range(2)]
        print(getMaxVal(n, stickers))

main()