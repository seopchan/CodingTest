# 1240 / 노드사이의 거리

"""
트리에서 두 노드 사이의 거리 구하기

DFS를 이용해 거리 계산
"""

import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10000)

def readInput():
    N, M = map(int, input().split())
    edges = [tuple(map(int, input().strip().split())) for _ in range(N-1)]
    targets = [tuple(map(int, input().strip().split())) for _ in range(M)]
    return N, M, edges, targets

def createGraph(N, edges):
    graph = defaultdict(list)
    for a, b, d in edges:
        graph[a].append((b, d))
        graph[b].append((a, d))
    return graph

def dfs(node, parent):
    for neighbor, weight in graph[node]:
        if neighbor != parent:
            # 현재 노드의 깊이에 1을 더해 이웃 노드의 깊이 설정
            depth[neighbor] = depth[node] + 1 
            # 현재 노드까지의 거리에 엣지의 가중치를 더해 이웃 노드까지의 거리 설정
            distance[neighbor] = distance[node] + weight 
            # 이웃 노드의 부모를 현재 노드로 설정
            parents[neighbor] = node 
            dfs(neighbor, node)

def main():
    N, M, edges, targets = readInput()
    global graph, depth, distance, parents
    graph = createGraph(N, edges)
    
    # 각 노드의 깊이를 저장
    depth = [-1] * (N + 1)
    
    # 루트 노드부터 각 노드까지의 거리를 저장
    distance = [0] * (N + 1)
    
    # 각 노드의 부모 노드를 저장
    parents = [-1] * (N + 1)
    
    # 루트 노드(1번 노드)의 깊이 0으로 설정
    depth[1] = 0
    dfs(1, -1)
    
    results = []
    for u, v in targets:
        # u에서 루트로 가는 경로상의 노드를 모두 방문 표시
        visited = set()
        copy = u
        while copy != -1:
            visited.add(copy)
            copy = parents[copy]
        
        # v에서 시작하여 u에서 루트로 가는 경로상에 있는 공통 조상을 찾음
        commonParent = v
        while commonParent not in visited:
            commonParent = parents[commonParent]
        
        # 두 노드 간의 거리는 각 노드의 루트까지의 거리 합에서 공통 조상까지의 거리의 두 배를 뺀 값
        dist = distance[u] + distance[v] - 2 * distance[commonParent]
        results.append(dist)
    
    for result in results:
        print(result)

main()