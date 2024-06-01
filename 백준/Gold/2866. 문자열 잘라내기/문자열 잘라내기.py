from sys import stdin

def findDuplicationInColumn(matrix, start_row):
    words = set()
    for col in range(len(matrix[0])):
        word = ''.join(matrix[row][col] for row in range(start_row, len(matrix)))
        if word in words:
            return True
        words.add(word)
    return False

r, c = map(int, stdin.readline().split())
table = [stdin.readline().strip() for _ in range(r)]

low, high = 0, r
result = r

# 이분탐색 적용
while low <= high:
    mid = (low + high) // 2
    if findDuplicationInColumn(table, mid):
        result = mid
        high = mid - 1
    else:
        low = mid + 1

# result는 중복이 발생한 인덱스
# 제거한 줄 수는 (result - 1)
print(result - 1)