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

def bfs(N, X, graph):
    # 모든 도시에 대한 최단거리를 초기화
    visited = [-1] * (N + 1)
    visited[X] = 0 # 시작도시의 거리는 0

    que = deque([X])

    while que:
        currentCity = que.popleft()

        for nextCity in graph[currentCity]:
            if visited[nextCity] == -1: # 방문하지 않은 도시
                visited[nextCity] = visited[currentCity] + 1
                que.append(nextCity)

    return visited

def main(N, K, X, roads):
    graph = defaultdict(list)

    # 그래프를 인접리스트로 표현
    for a, b in roads:
        graph[a].append(b)

    # BFS로 각 도시까지의 최단 거리 계산
    distance = bfs(N, X, graph)

    answer = sorted([city for city in range(1, N + 1) if distance[city] == K])

    if answer:
        for city in answer: print(city)
    else:
        print(-1)

# 데이터 입력
N, M, K, X = map(int, input().split())
roads = [tuple(map(int, input().strip().split())) for _ in range(M)]
main(N, K, X, roads)