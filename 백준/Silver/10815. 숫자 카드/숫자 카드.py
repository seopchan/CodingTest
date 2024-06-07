# 10815 / 숫자 카드

import sys
input = sys.stdin.readline

def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            print(1, end=' ')
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    print(0, end=' ')

N = int(input())
cards = list(map(int, input().strip().split()))
M = int(input())
targets = map(int, input().strip().split())

cards.sort()
for target in targets:
    binarySearch(cards, target)