# 11561 / 징검다리

# N -> 10^16 -> 이분탐색 고려

# 뒤에서부터 출발했을 때 N ~ -1씩 등차수열 
# -> N 을 초과하는 지점 찾기 -> 건널 수 없는 지점

import sys
input = sys.stdin.readline

def sumSequence(n):
    return n * (n + 1) / 2

def canReachN(n, maxJump):
    # maxJump번 내에서 N번 징검다리에 도착 가능한지 확인
    return sumSequence(maxJump) <= n
    
def binarySearch(n):
    left, right = 1, n
    answer = None

    while left <= right:
        mid = (left + right) // 2
        # print(n, mid, sumSequence(mid))
        if canReachN(n, mid):
            # n을 밟을 수 있으면
            # 많은 점프가 가능한지 확인
            answer = mid
            left = mid + 1
        else:
            # n을 밟을 수 없으면
            # 더 적은 점프면 가능한지 확인
            right = mid - 1
            
    return answer

def main(nums):
    for n in nums:
        print(binarySearch(n))

case = int(input())
nums = [int(input()) for _ in range(case)]
main(nums)