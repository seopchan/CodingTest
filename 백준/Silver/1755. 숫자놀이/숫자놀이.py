# 숫자를 1개씩 영어로 읽기
# 사전순으로 정렬

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

start, end = list(map(int, stdin.readline().split()))

changedList = []
changedDic = {}
for n in range(start, end + 1):
    numList = []
    for char in str(n):
        numList.append(numDic[char])
    
    changed = ' '.join(numList)
    changedDic[changed] = n
    changedList.append(changed)

changedList.sort()
for i, numStr in enumerate(changedList):
    print(changedDic[numStr], end=' ')
    if i % 10 == 9:
        print()