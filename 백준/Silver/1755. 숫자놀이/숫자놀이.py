# 튜플을 사용해 코드 간소화

from sys import stdin

numDic = ['zero','one','two','three','four','five','six','seven','eight','nine']

start, end = map(int, stdin.readline().split())

# 숫자를 영어로 변환하고 (영어, 숫자) 형태로 리스트에 저장
changedList = [
    (' '.join(numDic[int(char)] for char in str(n)), n)
    for n in range(start, end + 1)
]

changedList.sort()

for i, (numStr, originalNum) in enumerate(changedList):
    print(originalNum, end=' ')
    if i % 10 == 9:
        print()