# 4374 / 지프의 법칙

# 책에서 k번째로 많이 나온 단어의 출현 빈도
# 1/k에 비례

# 첫 번째 많이 나온 단어 1
# 두 번째 많이 나온 단어 첫 단어의 1/2
# 세 번째 많이 나온 단어 첫 단어의 1/3

# 딕셔너리로 등장 빈도 확인
# Set으로 n회 등장 단어 관리

import re
from sys import stdin
from collections import defaultdict

def isEndOfLine(input_line):
    return input_line.strip() == ''

def isEndOfText(input_text):
    return input_text.strip() == "EndOfText"

while True:
    input_line = stdin.readline().strip()
    if isEndOfLine(input_line): 
        break

    try:
        n = int(input_line)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        continue

    dic = defaultdict(int)
    appearedNTimes = set()

    while True:
        text = stdin.readline().strip()
        if isEndOfText(text): break

        # words = list(map(lambda word: word.strip(',').strip('.').strip('-').lower(), text.split()))
        words = re.findall(r'\b[a-z]+\b', text.lower())

        for word in words:
            if word:  # 공백 체크
                dic[word] += 1
                if dic[word] == n:
                    appearedNTimes.add(word)
                elif dic[word] > n:
                    appearedNTimes.discard(word)
    
    
    if appearedNTimes:
        appearedNTimesList = sorted(appearedNTimes)
        for word in appearedNTimesList:
            print(word)
    else:
        print("There is no such word.")
 
    print()