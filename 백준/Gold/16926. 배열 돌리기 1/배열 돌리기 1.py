# 16926 / 배열 돌리기 1

# 배열 사이즈 최대 300 * 300 = 90000
# 원소 최대 10억

# 규칙에 따라서 배열의 좌표를 바꾼 후
# 마지막에 바꾼 좌표에 맞는 새로운 배열 출력

# 테두리의 수 =  min(n, m) / 2

# 1. 테두리의 수 구하기
# 2. R에 따라서 좌표를 어떻게 이동하는지 계산
# 2-1. 테두리 찾기
# 3. 바뀐 좌표에 맞는 새로운 배열 출력


from sys import stdin

def countBorder(a, b):
    return min(a, b) // 2

# 테두리 추출 (시계방향)
def extractBorder(matrix, startR, startC, endR, endC):
    elements = []
    # Top row
    for j in range(startC, endC):
        elements.append(matrix[startR][j])
    # Right column
    for i in range(startR + 1, endR):
        elements.append(matrix[i][endC - 1])
    # Bottom row
    for j in range(endC - 2, startC - 1, -1):
        elements.append(matrix[endR - 1][j])
    # Left column
    for i in range(endR - 2, startR, -1):
        elements.append(matrix[i][startC])
    return elements

# r만큼 반시계 방향 회전
def rotateElements(elements, r):
    rotation = r % len(elements)
    return elements[rotation:] + elements [:rotation]

# 회전한 elements 다시 배치 (시계 방향)
def placeElements(matrix, elements, startRow, startCol, endRow, endCol):
    index = 0
    # Top row
    for j in range(startCol, endCol):
        matrix[startRow][j] = elements[index]
        index += 1
    # Right column
    for i in range(startRow + 1, endRow):
        matrix[i][endCol - 1] = elements[index]
        index += 1
    # Bottom row
    for j in range(endCol - 2, startCol - 1, -1):
        matrix[endRow - 1][j] = elements[index]
        index += 1
    # Left column
    for i in range(endRow - 2, startRow, -1):
        matrix[i][startCol] = elements[index]
        index += 1

# 테두리 돌리기
def rotateBorder(matrix, startR, startC, endR, endC, r):
    elements = extractBorder(matrix, startR, startC, endR, endC)
    rotatedElements = rotateElements(elements, r)
    placeElements(matrix, rotatedElements, startR, startC, endR, endC)

def main(N, M, R, matrix):
    borderCount = countBorder(N, M)

    # 테두리별로 Rotate
    for i in range(borderCount):
        startR, startC = i, i
        endR, endC = N - i, M - i
        rotateBorder(matrix, startR, startC, endR, endC, R)
    
    for row in matrix:
        print(' '.join(row))

N, M, R = map(int, stdin.readline().split())
matrix = [stdin.readline().strip().split() for _ in range(N)]
main(N, M, R, matrix)