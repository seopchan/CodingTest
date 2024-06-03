# 10868 / 최솟값

# 1 <= N <= 100,000
# (a, b) 100,000
# a~b까지 정수 중 가장 작은 정수 찾기
# 10만개를 10만번 탐색하면 시간 초과 10^10

# 구간의 최솟값
# 세그먼트 트리(특정한 범위의 데이터의 합 구하기) -> 이진트리
# 각 노드에 특정 구간의 최솟값 저장

# 트리 dict로 초기화
# 세그먼트 트리 생성
# - 데이터 list, 트리, 노드 인덱스, 범위의 시작, 끝
# - 리프노드 : list의 각 원소
# - 내부노드 : 두 자식 노드 중 최소값

from sys import stdin
from collections import defaultdict

# 재귀로 새그먼트 트리 구축
# 리프부터 시작해 상위 노드로 올라가며 구축
def createSegmentTree(list, tree, node, start, end):
    if start == end:
        tree[node] = list[start]
    else:
        mid = (start + end) // 2
        # 왼쪽 자식 노드
        createSegmentTree(list, tree, 2 * node, start, mid)
        # 오른쪽 자식 노드
        createSegmentTree(list, tree, 2 * node + 1, mid + 1, end)
        # 현재 노드 값은 두 자식 노드 중 작은 값
        tree[node] = min(tree[2 * node], tree[2 * node + 1])

# 트리를 탐색해 최솟값 찾기
def getMinInTree(tree, node, start, end, L, R):
    if R < start or end < L:
        # 탐색 구간과 노드 구간이 겹치지 않는 경우
        return float('inf')
    if L <= start and end <= R:
        # 탐색 구간이 노드를 완전히 포함
        return tree[node]
    
    mid = (start + end) // 2
    # 왼쪽 자식 노드 찾기
    leftMin = getMinInTree(tree, 2 * node, start, mid, L, R)
    rightMin = getMinInTree(tree, 2 * node + 1, mid + 1, end, L, R)
    # print(start,':', mid, '->', leftMin, mid + 1,':', end, '->', rightMin)
    return min(leftMin, rightMin)

def main(N, M, numList, rangeList):
    # 세그먼트 트리
    tree = defaultdict(int)

    # 세그먼트 트리 생성
    createSegmentTree(numList, tree, node = 1, start = 0, end = N-1)

    # 트리에서 범위 내 최소값 찾기
    for a, b in rangeList:
        minVal = getMinInTree(tree, node = 1, start = 0, end = N-1, L=a - 1, R=b - 1)
        print(minVal)

N, M = map(int, stdin.readline().split())
numList = [int(stdin.readline()) for _ in range(N)]
rangeList = [tuple(map(int, stdin.readline().split())) for _ in range(M)]

main(N, M, numList, rangeList)