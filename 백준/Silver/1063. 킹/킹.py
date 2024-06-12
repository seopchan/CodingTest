# 1063 / 킹

"""
row 1 ~ 8
col a ~ h

8방향 이동
"""
import sys
input = sys.stdin.readline

def posToIndex(pos):
    col = ord(pos[0]) - ord('A')
    row = int(pos[1]) - 1
    return (row, col)

def indexToPos(index):
    col = chr(index[1] + ord('A'))
    row = str(index[0] + 1)
    return col + row

# 범위 내에 있는지 확인
def isInBoard(pos):
    row, col = pos
    if 0 <= row < 8 and 0 <= col < 8:
        return True
    else:
        return False

def move(kingPos, stonePos, movesList):
    # 8방향 이동
    moves = {
        'R': (0, 1),
        'L': (0, -1),
        'B': (-1, 0),
        'T': (1, 0),
        'RT': (1, 1),
        'LT': (1, -1),
        'RB': (-1, 1),
        'LB': (-1, -1)
    }

    king = posToIndex(kingPos)
    stone = posToIndex(stonePos)

    for move in movesList:
        dx, dy = moves[move]
        newKing = (king[0] + dx, king[1] + dy)

        if isInBoard(newKing):
            if newKing == stone:
                newStone = (stone[0] + dx, stone[1] + dy)
                if isInBoard(newStone):
                    king = newKing
                    stone = newStone
            else:
                king = newKing

    print(indexToPos(king))
    print(indexToPos(stone))

kingPos, stonePos, N = input().strip().split()
movesList = [input().strip() for _ in range(int(N))]
move(kingPos, stonePos, movesList)