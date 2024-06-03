# 1018 / 체스판 다시 칠하기

# 조건
# M * N -> 8 * 8
# 1. (0, 0) 흰색 2. (0, 0) 검은색

# 1, 2번으로 만들기 -> 만들 때 칠해야하는 부분만 1
# 8 * 8 범위에서 1의 개수의 합 -> 최소 찾기
# 완전탐색

from sys import stdin

def findChangedWhenMakeNewBoard(N, M, board, baseColor, subColor):
    newBoard = [[False for _ in range(M)] for _ in range(N)]
    for r, line in enumerate(board):
        for c, color in enumerate(line):
            if (r + c) % 2:
                newBoard[r][c] = color == baseColor
            else:
                newBoard[r][c] = color == subColor
    return newBoard
                
def countPainting(board, N, M):
    minCount = 65
    # 슬라이딩 윈도우를 8 * 8 크기로 이동하며 True 세기
    for i in range(N - 7):
        for j in range(M - 7):
            count = 0
            # 8 * 8 부분의 True 개수 세기
            for c in range(8):
                for r in range(8):
                    if board[i + c][j + r]:
                        count += 1
            minCount = min(minCount, count)
    return minCount

def main(N, M, board):
    changedWhiteBoard = findChangedWhenMakeNewBoard(N, M, board, "W", "B")
    changedBlackBoard = findChangedWhenMakeNewBoard(N, M, board, "B", "W")
    
    paintWhiteCount = countPainting(changedWhiteBoard, N, M)
    paintBlackCount = countPainting(changedBlackBoard, N, M)

    print(min(paintWhiteCount, paintBlackCount))

N, M = map(int, stdin.readline().split())
board = [stdin.readline().strip() for _ in range(N)]
main(N, M, board)