# 10473 / 인간 대포

"""
a ~> b => 걷기 or 대포
대포 => 걷기 or 대포

걷기 : 5m/s => 50m : 10초
대포 : 25m/s => 50m : 2초

1. 최단경로
2. 2차원 배열
"""
import heapq
import sys
input = sys.stdin.readline

# 피타고라스의 정리
def calcDist(a, b):
    x1, y1 = a
    x2, y2 = b

    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# 거리 = 속력 * 시간
# 시간 = 거리 / 속력
def calcMoveTime(dist, isWithCannon):
    timeWithCannon = 2 + (abs(dist - 50) / 5)
    timeWithWalk = dist / 5
    if isWithCannon:
        return min(timeWithCannon, timeWithWalk)
    else:
        return timeWithWalk

def coordToTime(a, b, isWithCannon):
    return calcMoveTime(calcDist(a, b), isWithCannon)

def createGraph(pos, target, cannons, n):
    graph = [[] for _ in range(n + 2)]
    a, b = 0, n + 1
    # 1.pos to target
    graph[a].append((b, coordToTime(pos, target, False)))
    
    for i in range(n):
        # 2. pos to cannons
        graph[a].append((i + 1, coordToTime(pos, cannons[i], False)))
        # 3. cannons to cannons
        for j in range(i + 1, n):
            graph[i+1].append((j + 1, coordToTime(cannons[i], cannons[j], True)))
            graph[j+1].append((i + 1, coordToTime(cannons[i], cannons[j], True)))
        # 4. cannons to target
        graph[i+1].append((b, coordToTime(cannons[i], target, True)))

    return graph

def dijkstra(graph, n, startNode):
    times = [float('inf')] * (n + 1)
    times[startNode] = 0
    pq = [(0, startNode)]

    while pq:
        curTime, curNode = heapq.heappop(pq)

        if curTime > times[curNode]:
            continue
        
        for nbr, time in graph[curNode]:
            newTime = curTime + time

            if newTime < times[nbr]:
                times[nbr] = newTime
                heapq.heappush(pq, (newTime, nbr))

    print(f"{times[n - 1]:.6f}")

def main():
    pos = tuple(map(float, input().strip().split()))
    target = tuple(map(float, input().strip().split()))
    n = int(input())
    cannons = [tuple(map(float, input().strip().split())) for _ in range(n)]

    graph = createGraph(pos, target, cannons, n)

    dijkstra(graph, len(graph), 0)
    
main()