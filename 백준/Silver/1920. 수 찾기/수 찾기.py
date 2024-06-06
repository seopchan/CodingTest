# 1920 / 수 찾기

# N개의 정수 안에 x가 존재하는지 확인 
# -> 여러번 확인 -> 배열을 탐색하면 N * M
# -> 딕셔너리(해시)로 탐색 시간 1로 만들기 
# -> N개의 정수 중 있는지만 확인 -> set사용 메모리 줄이기

from sys import stdin

N = int(stdin.readline())
numSet = set(map(int, stdin.readline().split()))
M = int(stdin.readline())
arr = map(int, stdin.readline().split())

for i, num in enumerate(arr):
    print(1) if num in numSet else print(0)