# 10815 / 숫자 카드

"""
set
"""
import sys
input = sys.stdin.readline

N = int(input())
cards = set(map(int, input().strip().split()))
M = int(input())
targets = list(map(int, input().strip().split()))

results = []
for target in targets:
    if target in cards:
        results.append(1)
    else:
        results.append(0)

print(' '.join(map(str, results)))