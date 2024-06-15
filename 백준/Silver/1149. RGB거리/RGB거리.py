# 1149 / RGB거리
"""
i번째 집을 칠할 때 최소 비용: 
-> i-1번째 집을 다른 두 색으로 칠한 비용 중 작은 값 + i번째 집을 해당 색으로 칠하는 비용

i번째 집을 빨간색으로 칠하는 최소 비용
dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
초록
dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
파랑
dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])
"""

import sys
input = sys.stdin.readline

def main():
    N = int(input())
    costs = [list(map(int, input().strip().split()))  for _ in range(N)]
    
    dp = [[0]*3 for _ in range(N)]
    
    # 첫 집 rgb 각각 칠하기
    dp[0][0] = costs[0][0]
    dp[0][1] = costs[0][1]
    dp[0][2] = costs[0][2]
    
    # 점화식에 따라 DP 테이블 채우기
    for i in range(1, N):
        dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])
    
    # 마지막 집의 최소 비용 계산
    result = min(dp[N-1][0], dp[N-1][1], dp[N-1][2])
    print(result)

main()
