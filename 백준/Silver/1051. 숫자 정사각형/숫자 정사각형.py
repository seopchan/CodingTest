# 1051 / 숫자 정사각형

# N * M 
# 꼭짓점의 수가 모두 같은 가장 큰 정사각형

# 1 * 1 ~ min(N, M) * min(N, M)까지 다 탐색해보기

from sys import stdin

# 슬라이딩 윈도우를 X * Y 크기로 이동하며 처리
def isExistVerticesSameSqure(matrix, N, M, X, Y):
    for i in range(N - X + 1):
        for j in range(M - Y + 1):
            isVerticesSame = checkWindowVerticesSame(matrix, i, j, X, Y)
            if isVerticesSame:
                return True

# 윈도우 모서리 (꼭짓점) 요소 확인 및 처리 함수
def checkWindowVerticesSame(matrix, startRow, startCol, X, Y):
    vertices = set()
    
    # 윈도우의 네 모서리 좌표
    corners = [
        (startRow, startCol),
        (startRow, startCol + Y - 1),
        (startRow + X - 1, startCol),
        (startRow + X - 1, startCol + Y - 1)
    ]
    
    for r, c in corners:
        vertices.add(matrix[r][c])
    
    return len(vertices) == 1

def main(N, M, rectangle):
    maxSqureSize = min(N, M)
    # S * S 부터 2 * 2까지 확인 -> 없으면 1
    for length in range(maxSqureSize, 0, -1):
        if length == 1:
            print(1)
            break

        if isExistVerticesSameSqure(rectangle, N, M, length, length):
            print(length * length)
            break
    

N, M = map(int, stdin.readline().split())
rectangle = [stdin.readline().strip() for _ in range(N)]
main(N, M, rectangle)