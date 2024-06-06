# 21939 / 문제 추천 시스템 Version 1

# 번호, 난이도

# recommend(x)
#    x == 1 -> 최고 난이도, 큰 번호
#    x == -1 -> 최저 난이도, 작은 번호

# add(P, L)
#    난이도가 L인 문제 번호 P 추가
#    같은 문제 번호가 다른 난이도로 들어올 수 있음(난이도 변경)

# solved(P)
#    P 제거

# 1. 문제 번호, 난이도 저장 dict
# 2. recommend -> dict에서 최대/최소값 찾기
# 3. 최대힙, 최소힙 2개 관리

import heapq

questions = {}
maxHeap = []
minHeap = []

"""
dict에 문제 번호:난이도 추가
최대 힙 (-L, -P) 최소 힙 (L, P) 저장
"""
def addQuestion(P, L):
    questions[P] = L
    heapq.heappush(maxHeap, (-L, -P))
    heapq.heappush(minHeap, (L, P))

"""
questions 문제 번호 P 제거
최대힙, 최소힙과 동기화는 recommendQuestion에서 유효성 검사로 처리
"""
def solveQuestion(P):
    if P in questions:
        del questions[P]

"""
x가 1이면 최대 힙 pop
x가 -1이면 최소 힙 pop
최대 힙, 최소 힙에서 유효하지 않은 문제를 제거 -> 최대힙, 최소힙, questions의 동기화
questions에서 유효한 문제를 찾을 때까지 반복
"""
def recommendQuestion(x):
    if x == 1:
        while True:
            L, P = heapq.heappop(maxHeap)
            L, P = -L, -P
            if P in questions and questions[P] == L:
                heapq.heappush(maxHeap, (-L, -P))
                return P
    elif x == -1:
        while True:
            L, P = heapq.heappop(minHeap)
            if P in questions and questions[P] == L:
                heapq.heappush(minHeap, (L, P))
                return P

def main():
    N = int(input())
    for _ in range(N):
        P, L = map(int, input().split())
        addQuestion(P, L)

    M = int(input())
    for _ in range(M):
        command = input().split()
        if command[0] == "recommend":
            x = int(command[1])
            print(recommendQuestion(x))
        elif command[0] == "add":
            P, L = int(command[1]), int(command[2])
            addQuestion(P, L)
        elif command[0] == "solved":
            P = int(command[1])
            solveQuestion(P)

main()