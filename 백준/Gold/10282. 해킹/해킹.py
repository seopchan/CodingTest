# 10282 / 해킹
"""
의존성을 딕셔너리로 저장
매 시간마다 감염

1. 그래프로 만들기
2. heapq로 우선순위 큐 생성
3. 다익스트라로 최단 경로(최단 감염 시간) 계산
"""
import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline

def dijkstra(n, start, graph):
    dist = [float('inf')] * (n + 1) # pc가 1부터 시작
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        # 현재까지의 감염 시간이 가장 작은 경로부터 탐색
        curTime, curNode =  heapq.heappop(pq)

        if curTime > dist[curNode]:
            continue
        
        # 인접 노드 확인
        for nbr, time in graph.get(curNode, []):
            newTime = curTime + time
            if newTime < dist[nbr]:
                dist[nbr] = newTime
                heapq.heappush(pq, (newTime, nbr))

    infectedCount = sum(1 for d in dist if d < float('inf'))
    time = max(d for d in dist if d < float('inf'))

    return infectedCount, time

def createGraph(data):
    graph = defaultdict(list)
    for a, b, s in data:
        graph[b].append((a, s))
    return graph

def main():
    case = int(input())
    answer = []
    for _ in range(case):
        n, d, c = map(int, input().split())
        data = [tuple(map(int, input().strip().split())) for _ in range(d)]
        graph = createGraph(data)
        infectedCount, time = dijkstra(n, c, graph)
        print(infectedCount, time)

main()