# 10815 / 숫자 카드
"""
set
"""
import sys
input = sys.stdin.readline

N = int(input())
cards = set(map(int, input().strip().split()))
M = int(input())
targets = map(int, input().strip().split())

results = []
for target in targets:
    results.append('1') if target in cards else results.append('0')

print(' '.join(results))