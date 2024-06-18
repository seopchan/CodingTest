# 16236 / 아기 상어

"""
N * N, 물고기 M마리, 상어 1마리
자연수 크기, 상어 2

1초에 상하좌우 탐색, 큰 물고기 = 장애물

1. 먹을 수 있는 물고기가 없으면 도움 -> 끝
2. 1마리면 그 물고기 먹음
3. 2마리 이상이면 더 가까운 물고기 먹음
4. 같은 거리 여러마리면 위, 왼쪽 순으로

1. 사방탐색
2. 조건에 따라 이동 -> 구현, 시뮬레이션
"""
from collections import deque
import sys
input = sys.stdin.readline

def isInGrid(x, y, n):
    return 0 <= x < n and 0 <= y < n

def isPassable(grid, x, y, sharkSize):
    return grid[x][y] <= sharkSize

def bfs(grid, shark, sharkSize):
    n = len(grid)
    sr, sc = shark

    # 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    visited = [[-1] * n for _ in range(n)]

    q = deque()
    q.append((sr, sc, 0))
    visited[sr][sc] = 0
    eatables = []

    while q:
        r, c, dist = q.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if isInGrid(nr, nc, n) and visited[nr][nc] == -1 and isPassable(grid, nr, nc, sharkSize):
                visited[nr][nc] = dist + 1
                if 0 < grid[nr][nc] < sharkSize:
                    # 먹을 수 있으면
                    eatables.append((dist + 1, nr, nc))
                else:
                    # 못 먹으면, 이어서 탐색
                    q.append((nr, nc, dist + 1))
    
    if eatables:
        eatables.sort() # 먹을 수 있는 물고기들을 거리, 행(위), 열(왼쪽) 순으로 정렬
        return (eatables[0][1], eatables[0][2]), eatables[0][0]
    else:
        return None, -1


def eatFishes(grid, sharkPos):
    sharkSize = 2
    totalTime = 0
    eatCount = 0
    
    while True:
        newSharkPos, time = bfs(grid, sharkPos, sharkSize)
        if time == -1:
            break

        nr, nc = newSharkPos
        totalTime += time
        eatCount += 1
        grid[sharkPos[0]][sharkPos[1]] = 0
        grid[nr][nc] = 0
        sharkPos = (nr, nc)

        if eatCount == sharkSize:
            sharkSize += 1
            eatCount = 0

    # 2. 더 이상 못 먹으면
    print(totalTime)

def main():
    n = int(input())
    sharkPos = None
    grid = []
    for r in range(n):
        row = list(map(int, input().strip().split()))
        grid.append(row)
        for c, n in enumerate(row):
            if n == 9:
                sharkPos = (r, c)
                grid[r][c] = 0

    eatFishes(grid, sharkPos)

main()