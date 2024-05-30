# 어느 땅에서 한 번호가 절반을 초과하면 해당 번호가 지배
# 지배되지 않았으면 SYJKGW 출력

from sys import stdin
from collections import defaultdict

N = int(stdin.readline())
for _ in range(N):
    data = stdin.readline().split()

    peopleCount = int(data[0])
    peopleList = list(map(int, data[1:]))

    mapData = defaultdict(int)
    for num in peopleList:
        mapData[num] += 1

    half = peopleCount / 2
    overHalf = False
    for key, val in mapData.items():
        if val > half:
            print(key)
            overHalf = True
            break
    if not overHalf:
        print("SYJKGW")