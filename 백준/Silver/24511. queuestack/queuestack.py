# 24511 / queuestack

# queuestack

# x(n)을 n + 1번 자료구조에 append -> pop -> x(n+1) 

# 2번 줄: 큐, 스택 타입 구분
# 3번 줄: 2번줄의 데이터
# 5번줄: 작업을 할 데이터

# 스택은 무시

from sys import stdin
from collections import deque

# 데이터 읽어오기
N = int(stdin.readline().strip())
typeList = map(int, stdin.readline().split())
initialValues = list(map(int, stdin.readline().split()))
M = int(stdin.readline().strip())
numList = map(int, stdin.readline().split())

deq = deque()

for i, t in enumerate(typeList):
    if t == 0:
        deq.append(initialValues[i])

answer = []
for num in numList:
    deq.appendleft(num)
    answer.append(str(deq.pop()))

print(' '.join(answer))