# 4374 / 지프의 법칙

# 딕셔너리로 등장 빈도 확인
# Set으로 n회 등장 단어 관리

import re
from sys import stdin
from collections import defaultdict

while True:
    input_line = stdin.readline().strip()
    if not input_line: 
        break

    n = int(input_line)

    dic = defaultdict(int)
    appearedNTimes = set()

    while True:
        text = stdin.readline().strip()
        if text == "EndOfText": break

        # 단어 경계에서 소문자 단어 추출, 대소문자 구분 x
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