# 2346 / 풍선 터뜨리기

# 1~N 원형 큐 -> 큐의 크기가 바뀜
# 1번 터뜨린 후 

from sys import stdin
from collections import deque

N = int(stdin.readline())
list = map(int, stdin.readline().split())

deq = deque((i + 1, num) for i, num in enumerate(list))

popedList = []
while deq:
    idx, r = deq.popleft()
    # 우측으로 이동 시 풍선이 터지며 넘어간 인덱스 -1
    if r >= 0:
        r -= 1
    
    popedList.append(str(idx))
    deq.rotate(-r)

print(' '.join(popedList))