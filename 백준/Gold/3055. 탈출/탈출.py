# 3055 / 탈출

from collections import deque

def isWithBounds(x, y):
    return 0 <= x < r and 0 <= y < c

def initCoords(forest):
    waterCoords = []
    dochiStart = None
    times = {'water': [[-1] * c for _ in range(r)], 'dochi': [[-1] * c for _ in range(r)]}
    
    for i in range(r):
        for j in range(c):
            if forest[i][j] == '*':
                waterCoords.append((i, j))
                times['water'][i][j] = 0
            elif forest[i][j] == 'S':
                dochiStart = (i, j)
                times['dochi'][i][j] = 0

    return waterCoords, dochiStart, times

def bfs(forest, waterCoords, dochiStart, times):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    waterQue = deque(waterCoords)
    dochiQue = deque([dochiStart])
    
    while waterQue or dochiQue:
        newWaterQue = deque()
        while waterQue:
            x, y = waterQue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if isWithBounds(nx, ny) and forest[nx][ny] == '.' and times['water'][nx][ny] == -1:
                    times['water'][nx][ny] = times['water'][x][y] + 1
                    newWaterQue.append((nx, ny))
        waterQue = newWaterQue

        newDochiQue = deque()
        while dochiQue:
            x, y = dochiQue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if isWithBounds(nx, ny):
                    if forest[nx][ny] == 'D':
                        return times['dochi'][x][y] + 1
                    if forest[nx][ny] == '.' and times['dochi'][nx][ny] == -1:
                        if times['water'][nx][ny] == -1 or times['dochi'][x][y] + 1 < times['water'][nx][ny]:
                            times['dochi'][nx][ny] = times['dochi'][x][y] + 1
                            newDochiQue.append((nx, ny))
        dochiQue = newDochiQue

    return "KAKTUS"

def main(forest):
    waterCoords, dochiStart, times = initCoords(forest)
    print(bfs(forest, waterCoords, dochiStart, times))

global r, c
r, c = map(int, input().split())
forest = [input().strip() for _ in range(r)]
main(forest)