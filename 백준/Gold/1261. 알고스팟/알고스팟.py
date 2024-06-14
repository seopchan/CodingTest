# 1261 / 알고스팟
"""
미로 2차원 배열
가중치 : 벽을 부순 횟수
시작점 1,1

가중치 존재, 최단경로 -> 다익스트라 사용
"""
import heapq as hq
import sys
input = sys.stdin.readline

def isInMaze(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def dijkstra(n, m, maze):
    # 상 하 좌 우
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    pq = []
    hq.heappush(pq, (0, 0, 0)) # 벽 부순 횟수, x, y
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True

    while pq:
        walls, x, y = hq.heappop(pq)

        # 목적지 도착
        if x == n-1 and y == m-1:
            return walls
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if isInMaze(nx, ny, n, m) and not visited[nx][ny]:
                visited[nx][ny] = True
                if maze[nx][ny] == 1:
                    hq.heappush(pq, (walls + 1, nx, ny))
                else:
                    hq.heappush(pq, (walls, nx, ny))

def main():
    m, n = map(int, input().split())  # 가로 M, 세로 N
    maze = [list(map(int, input().strip())) for _ in range(n)]
    print(dijkstra(n, m, maze))

main()