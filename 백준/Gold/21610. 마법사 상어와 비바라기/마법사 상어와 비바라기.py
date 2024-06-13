# 21610 / 마법사 상어와 비바라기

"""
파이어볼, 토네이도, 파이어스톰, 물복사버그


N * N 각 칸에는 바구니, 첫 행 / 첫 열과 끝 행/ 끝 열은 연결되어 있음 %연산
비바라기 (N, 1) (N, 2) (N-1, 1) (N-1, 2) -> 비구름

1. 구름 d방향 s거리 이동
2. 비가 내림
3. 구름 사라짐
4. 물이 증가한 칸에 물복사 버그, 대각선 방향 거리1인 칸에 물이 있는 바구니의 수만큼 물의 양 증가
    이동과 다르게 맵을 넘어가지 않음
5. 바구니에 저장된 물의 양이 2이상인 모든 칸에 구름이 생기고, 물의 양 2감소 단, 3에서 사라진 칸은 아니어야 함
"""

import sys
input = sys.stdin.readline

# 8방향 (r, c) ←, ↖, ↑, ↗, →, ↘, ↓, ↙
DIRECTIONS = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

def isInGrid(r, c, N):
    return 0 <= r < N and 0 <= c < N

def hopeRain(N):
    posList = [(N, 1), (N, 2), (N-1, 1), (N-1, 2)]
    clouds = []
    for r, c in posList:
        zeroR, zeroC = r - 1, c - 1
        clouds.append((zeroR, zeroC))
    
    return clouds

def moveCloud(N, clouds, d, s):
    movedClouds = []
    for cloud in clouds:
        r, c = cloud
        dr, dc = DIRECTIONS[d - 1]

        for _ in range(s):
            r, c = (r + dr + N) % N, (c + dc + N) % N
        movedClouds.append((r, c))

    return movedClouds

def rainDrop(grid, clouds):
    for cloud in clouds:
        r, c = cloud
        grid[r][c] += 1

def waterCopy(grid, N, coords):
    # 대각선 -> DIRECTIONS -> 1, 3, 5, 7
    for r, c in coords:
        increment = 0
        for d in range(1, 8, 2):
            dr, dc = DIRECTIONS[d]
            newR, newC = r + dr, c + dc
            if isInGrid(newR, newC, N):
                if grid[newR][newC] > 0:
                    increment += 1
        
        grid[r][c] += increment

def waterToCloud(grid, N, prevClouds):
    newClouds = []
    for r in range(N):
        for c in range(N):
            if grid[r][c] >= 2 and (r, c) not in prevClouds:
                grid[r][c] -= 2
                newClouds.append((r, c))

    return newClouds   

def printGrid(grid):
    print()
    for row in grid:
        print(row)
    print()

def main():
    N, M = map(int, input().split())
    grid = [list(map(int, input().strip().split())) for _ in range(N)]
    commands = [map(int, input().strip().split()) for _ in range(M)]

    clouds = hopeRain(N)
    for d, s in commands:
        clouds = moveCloud(N, clouds, d, s)
        
        rainDrop(grid, clouds)

        increaseWaterList = clouds
        waterCopy(grid, N, increaseWaterList)

        clouds = waterToCloud(grid, N, set(clouds))

    totalWater = 0
    for row in grid:
        totalWater += sum(row)

    print(totalWater)

main()