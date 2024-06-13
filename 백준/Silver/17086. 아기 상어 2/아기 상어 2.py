# 17086 / 아기 상어 2

"""
N * M 1칸당 최대 1마리
안전거리 : 8방향으로 가장 가까운 상어와 거리

BFS로 각 칸에서 가장 가까운 아기 상어 찾기
"""
from collections import deque
import sys
input = sys.stdin.readline

def isInBox(x, y, N, M):
    return 0 <= x < M and 0 <= y < N

def findMaxDistance(grid, N, M):
    maxVal = 0
    for i in range(N):
        for j in range(M):
            maxVal = max(maxVal, grid[i][j])
    return maxVal


def bfs(grid, N, M):
    # 8방향 위부터 시계방향
    dir = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

    # 방문처리 및 거리 저장
    visited = [[-1] * M for _ in range(N)]

    # BFS위한 큐
    q = deque()

    # 상어 위치 거리 0으로 설정
    for y in range(N):
        for x in range(M):
            if grid[y][x] == 1:
                q.append((x, y))
                visited[y][x] = 0
    
    while q:
        x, y = q.popleft()

        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            # 범위 내에 있고, 방문하지 않았고, 상어가 아니면
            if isInBox(nx, ny, N, M) and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                q.append((nx, ny))
    
    print(findMaxDistance(visited, N, M))

def main():
    N, M = map(int, input().split())
    grid = [list(map(int, input().strip().split())) for _ in range(N)]

    bfs(grid, N, M)

main()