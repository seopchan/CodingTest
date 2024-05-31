# 1764 / 듣보잡

# 듣못 / 보못 -> 듣보못
# 듣못과 보못의 교집합
# 사전순 정렬

from sys import stdin

n, m = map(int, stdin.readline().split())

neverHeard = set()
for _ in range(n):
    neverHeard.add(stdin.readline().strip())

neverHeardSeen = set()
for _ in range(m):
    name = stdin.readline().strip()
    if name in neverHeard:
        neverHeardSeen.add(name)

print(len(neverHeardSeen))
for name in sorted(neverHeardSeen):
    print(name)