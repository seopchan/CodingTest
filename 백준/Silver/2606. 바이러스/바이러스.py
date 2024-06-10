# 2606 / 바이러스

"""
주어진 컴퓨터 네트워크를 그래프 자료구조로 변환
1번 컴퓨터부터 시작, 연결된 모든 컴퓨터 탐색
-> 모든 컴퓨터를 탐색하므로 DFS, BFS 모두 사용 가능

DFS 사용

1. 인접 리스트 그래프 만들기
2. DFS 탐색
3. 1번 컴퓨터를 제외한 방문 컴퓨터의 수 출력
"""
from collections import defaultdict
import sys
input = sys.stdin.readline

def dfs(graph, startNode, visited):
    stack = [startNode]
    visited[startNode] = True
    count = 0

    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
                count += 1
    return count

def main(n, connections):
    graph = defaultdict(list)
    for a, b in connections:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [False] * (n + 1)
    print(dfs(graph, 1, visited))

# 데이터 입력
numComputers = int(input())
numConnections = int(input())
connections = [tuple(map(int, input().strip().split())) for _ in range(numConnections)]
main(numComputers, connections)