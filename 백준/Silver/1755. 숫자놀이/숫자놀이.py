# 튜플을 사용해 코드 간소화

from sys import stdin

numDic = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

start, end = map(int, stdin.readline().split())

# 숫자를 영어로 변환하고 (영어, 숫자) 형태로 리스트에 저장
changedList = [
    (' '.join(numDic[char] for char in str(n)), n)
    for n in range(start, end + 1)
]

changedList.sort()

for i, (numStr, originalNum) in enumerate(changedList):
    print(originalNum, end=' ')
    if i % 10 == 9:
        print()