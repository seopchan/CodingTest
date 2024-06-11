"""
2 <= N <= 10000 섬
섬 사이 다리
-> vertex, edge

bfs로 탐색 -> 탐색하며 최대 중량 확인 
-> 같은 두 섬 사이에 여러 다리가 있을 수 있음

1. 단순히 최대 무게를 따라가기
-> 이후에 더 작은 경로가 나오면 더이상 최적의 경로가 아님

2. 한 번의 이동에서 옮길 수 있는 최댓값
-> 모든 가능한 경로를 고려해야 함

* 중량의 최댓값 찾기 *
중량이 10억 -> 이분탐색?

중량을 이분탐색하며
-> 해당 중량으로 이동할 수 있는 경로 확인을 bfs로 하기
"""

from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def createGraph(bridges):
    graph = defaultdict(list)
    MAX_WEIGHT = 0
    for a, b, weight in bridges:
        graph[a].append((b, weight))
        graph[b].append((a, weight))
        if weight > MAX_WEIGHT:
            MAX_WEIGHT = weight

    return graph, MAX_WEIGHT

def bfs(graph, start, end, weight):
    visited = set()
    q = deque([start])

    while q:
        node = q.popleft()

        # 중량 싣고 도착 가능
        if node == end:
            return True

        if node not in visited:
            visited.add(node)
            for neighbor, nWeight in graph[node]:
                if neighbor not in visited and nWeight >= weight:
                    q.append(neighbor)

    return False

def binarySearch(MAX_WEIGHT, bfsData):
    graph, start, end = bfsData
    l, r = 1, MAX_WEIGHT

    while l <= r:
        mid = (l + r) // 2

        # 중량을 싣고 도착이 가능하면 더 싣고 가능한지 확인
        if bfs(graph, start, end, mid):
            l = mid + 1
        else:
            r = mid - 1

    print(r)

def main(bridges, start, end):
    # 양방향 그래프 생성
    graph, MAX_WEIGHT = createGraph(bridges)
    binarySearch(MAX_WEIGHT, (graph, start, end))
    

N, M = map(int, input().strip().split())
bridges = [tuple(map(int, input().strip().split())) for _ in range(M)]
start, end = map(int, input().strip().split())
main(bridges, start, end)