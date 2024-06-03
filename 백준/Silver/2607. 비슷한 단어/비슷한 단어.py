# 2607 / 비슷한 단어

# 1. 한 문자 더하거나 빼기
# 2. 한 문자를 다른 문자로 바꾸기

# 카운터로 종류 계산
# (A - B) + (B - A)의 차이가 다른 부분의 수

from sys import stdin
from collections import Counter

def isSimilar(counter1, counter2):
    diff1 = sum((counter1 - counter2).values())
    diff2 = sum((counter2 - counter1).values())

    # 한 단어에 차이가 2개 이상 있는 경우
    if 1 < diff1 or 1 < diff2:
        return False
    
    # 한 단어에 차이가 1개 이하씩 있는 경우
    return diff1 + diff2 <= 2

def main(n, firstWord, words):
    similarCount = 0
    firstWordCounter = Counter(firstWord)
    for word in words:
        if isSimilar(firstWordCounter, Counter(word)):
            similarCount += 1

    print(similarCount)

n = int(stdin.readline())
firstWord = stdin.readline().strip()
words = [stdin.readline().strip() for _ in range(n - 1)]
main(n, firstWord, words)