"""
스택으로 DFS 구현
"""
from collections import defaultdict
import sys
input = sys.stdin.readline

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

def dfs(graph, start, fans):
    stack = [start]
    visited = set()
    
    while stack:
        node = stack.pop()
        if node in fans:
            continue
        if node in visited:
            continue
        visited.add(node)
        
        if not graph[node]:  # 리프 노드 도달
            return True
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)
    
    return False

def main():
    edges, fans = readInput()
    graph = createGraph(edges)

    if dfs(graph, 1, fans):
        print('yes')
    else:
        print('Yes')

main()