"""
수빈, 동생 0 ~ 100,000

가능한 모든 이동 == 인접 노드
BFS로 모든 인접노드 탐색
""" 
from collections import deque

def bfs(start, K, count):
    visited = set()
    q = deque([(start, 0)])

    while q:
        node, count = q.popleft()
        if node == K:
            return count

        if node not in visited:
            visited.add(node)
            neighbors = [node * 2, node - 1, node + 1]
            for neighbor in neighbors:
                if neighbor not in visited and 0 <= neighbor <= 100_000:
                    q.append((neighbor, count + 1))
            
def main(N, K):
    print(bfs(N, K, 0))

N, K = map(int, input().split())
main(N, K)