# 15650 / N과 M (2)

# 1 <= N <= M <= 8
# 1 ~ N까지 자연수 중 중복 없이 M개를 고른 수열
# 수열은 오름차순
# -> 조합으로 고르고 정렬

from sys import stdin
from itertools import combinations

n, m = map(int, stdin.readline().split())

combis = map(sorted, combinations(range(1, n + 1), m))
for combi in combis:
    print(" ".join(map(str, combi)))