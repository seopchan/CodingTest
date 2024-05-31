# 1764 / 듣보잡

# 듣못 / 보못 -> 듣보못
# 듣못과 보못의 교집합
# 사전순 정렬

from sys import stdin

n, m = map(int, stdin.readline().split())

neverHeard, neverSeen = set(), set()

for _ in range(n):
    neverHeard.add(stdin.readline().strip())

for _ in range(m):
    neverSeen.add(stdin.readline().strip())

neverHeardSeen = sorted(neverHeard & neverSeen)

print(len(neverHeardSeen))
for name in neverHeardSeen:
    print(name)