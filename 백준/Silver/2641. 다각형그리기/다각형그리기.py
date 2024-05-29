from collections import deque
# 원본, 순서 다른 배열과 비교
# reverse + 1 <-> 3, 2 <-> 4, 순서 다른 배열과 비교
# 순서 다른 배열은 deque으로 확인

def transform(sequence):
    return reversed([3 if x == 1 else 1 if x == 3 else 4 if x == 2 else 2 for x in sequence])

LEN = int(input())
origin = deque(map(int, input().split()))
originReversed = deque(transform(origin))
N = int(input())

answer = []
for _ in range(N):
    seq = deque(map(int, input().split()))

    for _ in range(LEN):
        if seq == origin or seq == originReversed:
            answer.append(' '.join(map(str, seq)))

        origin.append(origin.popleft())
        originReversed.append(originReversed.popleft())

print(len(answer))
for ans in answer:
    print(ans)