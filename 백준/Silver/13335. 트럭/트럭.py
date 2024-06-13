# 13335 / 트럭

"""
대기열, 다리의 트럭을 queue로 관리
대기가 있거나, 다리위에 트럭이 있다면
1. 다리에서 트럭을 빼고, 현재 무게 - 다리에서 빠진 트럭 무게
2. 새 트럭이 올라갈 수 있으면(현재 무게 + 다음 트럭 무게 <= 다리 무게), 다음 트럭 올림, 현재 무게 + 다음 트럭 무게
3. 시간 + 1
"""

from collections import deque
import sys
input = sys.stdin.readline

def main(bridgeLength, bridgeWeight, trucks):
    wait = deque(trucks)
    bridge = deque([0 for _ in range(bridgeLength)])
    
    time = 0
    currentWeight = 0
    while wait or currentWeight:
        # 1번
        currentWeight -= bridge.popleft()
        newTruck = 0
        
        # 2번
        if wait and currentWeight + wait[0] <= bridgeWeight:
            newTruck = wait.popleft()
            currentWeight += newTruck
        bridge.append(newTruck)

        # 3번
        time += 1
                
    print(time)

n, w, L = map(int, input().split())
trucks = map(int, input().strip().split())
main(w, L, trucks)