# 21937 / 작업

"""
작업 순서 그래프에서 특정 작업을 수행하기 위해 필요한 선행 작업의 개수
1. 역순 그래프 생성 -> 특정 작업부터 선행 작업 역순으로 탐색
2. 특정 작업에서 DFS로 모든 선행 작업 탐색
"""

from collections import defaultdict
import sys
input = sys.stdin.readline

def readInput():
    N, M = map(int, input().split())

    edges = [tuple(map(int, input().strip().split())) for _ in range(M)]
    X = int(input())
    return N, edges, X

def createGraph(N, edges):
    graph = defaultdict(list)
    for a, b in edges:
        # 단방향 그래프
        # 최종 작업부터 역순으로 확인해야하므로, 방향 reverse
        graph[b].append(a) 
    return graph

def dfs(graph, startNode):
    visited = set()
    stack = [startNode]
    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    return len(visited)

def main():
    N, edges, X = readInput()
    graph = createGraph(N, edges)
    print(dfs(graph, X))

main()