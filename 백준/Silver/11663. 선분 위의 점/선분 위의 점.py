# 11663 / 선분 위의 점

import sys
input = sys.stdin.readline

import sys
input = sys.stdin.readline

def binary_search_left(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

def binary_search_right(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

def main():
    N, M = map(int, input().split())
    points = list(map(int, input().split()))
    points.sort()
    
    results = []
    for _ in range(M):
        a, b = map(int, input().split())
        l = binary_search_left(points, a)
        r = binary_search_right(points, b)
        results.append(r - l)
    
    for result in results:
        print(result)

main()