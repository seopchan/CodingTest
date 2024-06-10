# 25195 / Yes or yes

"""
DAG(사이클이 없는 방향 그래프) 1번 노드에서 출발해
가능한 모든 경로를 탐색하며, 팬클럽을 만나는지 확인

1. 그래프를 탐색하며 리프 노드에 도달할 수 있는지 확인
2. 1번 노드부터 시작해 
    팬클럽을 만나지 않으면 yes 
    만나면 YES -> break

1. 팬클럽을 찾기 -> BFS
2. 경로를 찾기 -> DFS
-> 결국 경로를 찾기 위해 끝까지 탐색 -> DFS 사용
"""
from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def readInput():
    N, M = map(int, input().split())
    edges = [tuple(map(int, input().strip().split())) for _ in range(M)]
    S = int(input().strip())
    fans = set(map(int, input().strip().split()))
    return edges, fans

def createGraph(edges):
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
    return graph

def dfs(graph, node, fans, visited):
    if node in fans or node in visited:
        return False
    
    visited.add(node)

    if not graph[node]:  # 리프 노드 도달
        return True

    for neighbor in graph[node]:
        if dfs(graph, neighbor, fans, visited):
            return True

    return False

def main():
    edges, fans = readInput()
    graph = createGraph(edges)
    visited = set()

    if dfs(graph, 1, fans, visited):
        print('yes')
    else:
        print('Yes')

main()