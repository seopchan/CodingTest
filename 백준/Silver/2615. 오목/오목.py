# 2615 / 오목

# 19 * 19
# 5알 연속 -> 승, 6알 연속은 X

# 완전탐색

from sys import stdin
MAX = 19
overSix = {"ROW": set(), "COLUMN": set(), "RIGHTDOWN": set(), "LEFTDOWN": set()}

def checkRow(matrix, r, c, target):
    count = 0
    for i in range(c, MAX):
        if (r, i) in overSix["ROW"]:
            break

        if matrix[r][i] == target:
            count += 1
        else:
            break

    if count >= 6:
        for i in range(count):
            overSix["ROW"].add((r, c + i))
        return False
    elif count == 5:
        return True
    else: 
        return False   

def checkColumn(matrix, r, c, target):
    count = 0
    for i in range(r, MAX):
        if (i, c) in overSix["COLUMN"]:
            break

        if matrix[i][c] == target:
            count += 1
        else:
            break

    if count >= 6:
        for i in range(count):
            overSix["COLUMN"].add((r + i, c))
        return False
    elif count == 5:
        return True
    else: 
        return False     
    

def checkRightDown(matrix, r, c, target):
    count = 0
    i = 0
    while r + i < MAX and c + i < MAX:
        if (r + i, c + i) in overSix["RIGHTDOWN"]:
            break

        if matrix[r + i][c + i] == target:
            count += 1
        else:
            break
        i += 1
    
    if count >= 6:
        for i in range(count):
            overSix["RIGHTDOWN"].add((r + i, c + i))
        return False
    elif count == 5:
        return True
    else: 
        return False

def checkLeftDown(matrix, r, c, target):
    count = 0
    i = 0
    while r + i < MAX and c - i >= 0:
        if (r + i, c - i) in overSix["LEFTDOWN"]:
            break

        if matrix[r + i][c - i] == target:
            count += 1  
        else:
            break
        i += 1
            
    if count >= 6:
        for i in range(count):
            overSix["LEFTDOWN"].add((r + i, c - i))
        return False
    elif count == 5:
        return True
    else: 
        return False

def checkWin(matrix):
    for r, row in enumerate(matrix):
        for c, stone in enumerate(row):
            if stone == '0':
                continue
            # 1. 가로 5개
            # (x, y) (x + 4, y)
            if checkRow(matrix, r, c, stone):
                print(stone)
                print(r + 1, c + 1)
                return

            # 2. 세로 5개
            # (x, y) (x, y + 4)
            if checkColumn(matrix, r, c, stone):
                print(stone)
                print(r + 1, c + 1)
                return

            # 3. 정대각선 5개
            # (x, y) (x + 4, y + 4)
            if checkRightDown(matrix, r, c, stone):
                print(stone)
                print(r + 1, c + 1)
                return

            # 4. 역대각선 5개
            # (x, y) (x + 4, y - 4)
            if checkLeftDown(matrix, r, c, stone):
                print(stone)
                print(r + 1 + 4, c + 1 - 4)
                return
    print(0)

matrix = [stdin.readline().split() for _ in range(19)]

checkWin(matrix)