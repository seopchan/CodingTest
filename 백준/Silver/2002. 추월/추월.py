# 2002 / 추월

# FIFO를 어기면 : 추월했음

from sys import stdin

n = int(stdin.readline().strip())

enterOrder = [stdin.readline().strip() for _ in range(n)]
exitOrder = [stdin.readline().strip() for _ in range(n)]

# 나간 순서에 따른 각 차량의 인덱스 저장
exitIndex = {car: i for i, car in enumerate(exitOrder)}

overtakeCount = 0

# 현재까지 처리한 차량의 최대 인덱스를 추적
exitedCar = -1

# 들어온 순서대로 차량을 처리하면서 나간 순서와 비교
for car in enterOrder:
    carExitIndex = exitIndex[car]
    
    # 현재 차량의 나간 순서 인덱스가 지금까지의 최대 인덱스보다 작으면 추월한 것
    if carExitIndex < exitedCar:
        overtakeCount += 1
    else:
        exitedCar = carExitIndex

print(overtakeCount)