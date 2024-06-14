# 4485 / 녹색 옷 입은 애가 젤다지?

"""
그래프 탐색
동굴의 각 칸: vertex 이동: edge
가중치: 도둑 루피의 크기 0~9 양수

동굴의 제일 왼쪽 위부터 최소 비용 소모 탐색
-> 다익스트라 알고리즘 적용
"""

import heapq as hq
import sys
input = sys.stdin.readline

def isInCave(x, y, n):
    return 0 <= x < n and 0 <= y < n

def dijkstra(n, graph):
    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 각 칸까지의 최소 비용
    costs = [[float('inf')] * n for _ in range(n)]

    # 비용, x, y
    pq = [(graph[0][0], 0, 0)]

    while pq:
        curCost, x, y = hq.heappop(pq)

        # 이미 처리된 비용보다 큰 비용의 경로는 무시
        if curCost > costs[x][y]:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if isInCave(nx, ny, n):
                newCost = curCost + graph[nx][ny]
                # 더 작은 비용으로 이동할 수 있으면 갱신하고 큐에 추가
                if newCost < costs[nx][ny]:
                    costs[nx][ny] = newCost
                    hq.heappush(pq, (newCost, nx, ny))
    return costs[n-1][n-1]

def main():
    case = 1

    while True:
        n = int(input())
        if n == 0:
            break

        graph = [list(map(int, input().strip().split())) for _ in range(n)]

        cost = dijkstra(n, graph)
        print(f"Problem {case}: {cost}")
        case += 1

main()