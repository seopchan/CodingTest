# 1706 / 크로스워드

# 모든 단어 다 찾기
# 단어는 가로에서만 찾기 -> 배열 돌리기 (반시계 90도)

from sys import stdin

def getWordsInLine(line):
    words = []
    word = []
    for c in line:
        if c != '#':
            word.append(c)
        else:
            if len(word) > 0:
                if len(word) > 1:
                    words.append(''.join(word))
                word.clear()
    if len(word) > 1:
            words.append(''.join(word))
    return words

def getWordsInMatrix(matrix):
    words = []
    for line in matrix:
        words.extend(getWordsInLine(line))
    return words

def rotate90CounterClockwise(matrix):
    return [list(row) for row in zip(*matrix)][::-1]
     
def main():
    r, c = map(int, stdin.readline().split())
    puzzle = []

    for _ in range(r):
        line = stdin.readline().strip()
        puzzle.append(line)

    words = getWordsInMatrix(puzzle)

    # 반시계 90도 회전
    rotatedPuzzle = rotate90CounterClockwise(puzzle)

    words.extend(getWordsInMatrix(rotatedPuzzle))
    words.sort()
    print(words[0])

main()