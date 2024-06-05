# 1080 / 행렬

# 0, 1 행렬 A, B

# A -> B로 바꾸는데 필요한 연산의 횟수의 최솟값

# 3*3 순회하며 다르면 바로 바꾸기

from sys import stdin

# 3 * 3 모두 뒤집음
def flip(matrix, r, c):
    for i in range(r, r+3):
        for j in range(c, c+3):
            matrix[i][j] = (matrix[i][j] + 1) % 2

def main(mA, mB, N, M):
    count = 0

    # 3*3 순회 -> 다르면 바꿈
    for i in range(N-2):
        for j in range(M - 2):
            if mA[i][j] != mB[i][j]:
                flip(mA, i, j)
                count += 1
    
    print(count) if mA == mB else print(-1)
 
N, M = map(int, stdin.readline().split())

matrixA = [list(map(int, list(stdin.readline().strip()))) for _ in range(N)]
matrixB = [list(map(int, list(stdin.readline().strip()))) for _ in range(N)]

main(matrixA, matrixB, N, M)