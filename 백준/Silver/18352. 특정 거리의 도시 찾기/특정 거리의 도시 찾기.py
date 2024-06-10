# 18352 / 특정 거리의 도시 찾기

"""
단일 출발 도시에서 다른 도시들까지 최단 거리 계산
그 중 K 거리를 가지는 도시 찾기

최단 거리 찾기 -> BFS

1. 그래프 인접리스트로 표현
2. BFS로 거리 탐색
3. 거리가 K인 도시들을 오름차순 출력
"""

from collections import deque, defaultdict
import sys
input = sys.stdin.readline

def bfs(K, X, graph):
    # 방문 내역을 딕셔너리로 관리
    visited = {X: 0}
    que = deque([X])
    distanceK = []

    while que:
        currentCity = que.popleft()

        for nextCity in graph[currentCity]:
            if nextCity not in visited: # 방문하지 않은 도시
                newDistance = visited[currentCity] + 1
                visited[nextCity] = newDistance
                # 거리가 정확하게 K인 도시만 별도로 저장
                if newDistance == K:
                    distanceK.append(nextCity)
                
                # 거리가 K 이상이 되면 탐색 중지
                if newDistance < K:
                    que.append(nextCity)

    return distanceK

def main(K, X, roads):
    graph = defaultdict(list)

    # 그래프를 인접리스트로 표현
    for a, b in roads:
        graph[a].append(b)

    # BFS로 각 도시까지의 최단 거리 계산
    distanceK = sorted(bfs(K, X, graph))

    if distanceK:
        for city in distanceK: print(city)
    else:
        print(-1)

# 데이터 입력
N, M, K, X = map(int, input().split())
roads = [tuple(map(int, input().strip().split())) for _ in range(M)]
main(K, X, roads)