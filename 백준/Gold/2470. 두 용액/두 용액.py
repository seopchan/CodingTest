# 2470 / 두 용액

# 용액의 특성 / 산성 1 ~ 10억 / 염기성 -10억 ~ -1
# 혼합 -> A특성 + B특성

# 0에 가까운 용액 만들기
# -999,999,999 ~ 999,999,999 -> 혼합 범위

# 용액 2 ~ 10만개
# 특성값 정렬

"""
투포인터
"""
def find_closest_to_zero(n, num):
    left = 0
    right = n - 1
    
    closest_sum = float('inf')
    pair = (num[left], num[right])
    
    while left < right:
        current_sum = num[left] + num[right]
        
        # 현재의 합이 더 0에 가까우면 갱신
        if abs(current_sum) < abs(closest_sum):
            closest_sum = current_sum
            pair = (num[left], num[right])
        
        # 합이 0보다 크면 오른쪽 포인터를 왼쪽으로 이동
        if current_sum > 0:
            right -= 1
        # 합이 0보다 작으면 왼쪽 포인터를 오른쪽으로 이동
        elif current_sum < 0:
            left += 1
        # 합이 정확히 0이면 탐색 종료
        else:
            break
    
    return pair

N = int(input())
solutions = list(map(int, input().split()))

solutions.sort()
answer = find_closest_to_zero(N, solutions)
print(answer[0], answer[1])