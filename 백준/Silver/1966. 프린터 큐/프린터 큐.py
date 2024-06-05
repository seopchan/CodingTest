# 1966 / 프린터 큐

# 1. 중요도 확인
# 2. 중요도 낮은 문서는 Queue로

# 우선순위를 정렬해둔 배열 
#   -> 포인터 사용 -> 매번 큐를 탐색하지 않아도 됨
# queue를 사용

from sys import stdin
from collections import deque

case = int(stdin.readline())
for _ in range(case):
    n, targetIdx = map(int, stdin.readline().split())
    task = list(map(int, stdin.readline().split()))

    prioritys = sorted(task, reverse= True)
    queue = deque()
    # 출력 문서의 인덱스가 타겟 인덱스인지 확인하기 위해 (index, priority)로 변환
    for i, priority in enumerate(task):
        queue.append((i, priority))

    count = 0
    while queue:
        # 맨 앞 문서의 중요도 확인
        if queue[0][1] == prioritys[count]:
            # 중요도가 가장 높은 문서면 출력
            count += 1
            i, priority = queue.popleft()

            if i == targetIdx:
                print(count)
                break
        else:
            # 중요도가 더 높은 문서가 있으면 맨 뒤에 삽입
            queue.append(queue.popleft())