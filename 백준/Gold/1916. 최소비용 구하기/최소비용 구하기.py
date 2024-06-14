# 1916 / 최소비용 구하기

"""
도시 그래프, 비용 최소화
모든 버스 비용은 0 이상의 양수

1. 가중치가 있는 그래프(비용)
2. 단일 출발점 A부터 다른 모든 정점까지 최소비용 경로 탐색
-> 다익스트라 알고리즘 사용

1. 그래프 생성 -> 출발지:(도착지, 비용)
2. 다익스트라 -> 우선순위 큐 사용
"""
import heapq as hq
from collections import defaultdict
import sys
input = sys.stdin.readline

def dijkstra(n, graph, start):
    costs = [float('INF')] * (n + 1)
    costs[start] = 0
    pq = [(0, start)]

    while pq:
        curCost, curNode = hq.heappop(pq)

        if curCost > costs[curNode]:
            continue

        for end, cost in graph.get(curNode, []):
                newCost = curCost + cost

                if newCost < costs[end]:
                     costs[end] = newCost
                     hq.heappush(pq, (newCost, end))
    return costs

def createGraph(data):
    graph = defaultdict(list)
    for start, end, cost in data:
        graph[start].append((end, cost))
    return graph

def main():
    n = int(input())
    m = int(input())

    data = list(tuple(map(int, input().strip().split())) for _ in range(m))
    graph = createGraph(data)

    start, end = map(int, input().strip().split())
    costs = dijkstra(n, graph, start)
    print(costs[end])

main()