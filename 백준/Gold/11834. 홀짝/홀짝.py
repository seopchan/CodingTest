# 11834 / 홀짝

"""
홀: 1, 짝:2 시작점 설정

N 10^100 -> 이분탐색

"""
# 이분 탐색으로 N이 속하는 그룹 찾기
def binarySearch(N):
    left, right = 0, N
    group = 0
    while left <= right:
        mid = (left + right) // 2
        # 각 그룹의 마지막 인덱스를 계산
        groupLastIdx = mid * (mid + 1) // 2  
        if groupLastIdx >= N:
            group = mid
            right = mid - 1
        else:
            left = mid + 1
    return group

# 특정 그룹 내에서 N번째 요소의 값을 계산
def calcValue(N, group):
    """
    # 현재 그룹까지 포함된 총 요소 수
    totalElements = (group * (group + 1)) // 2
    # 그룹 내에서 N번째 위치
    positionInGroup = totalElements - N
    if group % 2 == 1:  # 홀수 그룹일 경우
        val = group ** 2 - 2 * positionInGroup
    else:  # 짝수 그룹일 경우
        val = (group ** 2 + 1) + 2 * positionInGroup
    return val
    """
    # 위의 수식을 정리하면
    return 2 * N - group

def main():
    print(calcValue(N, binarySearch(N)))

N = int(input())
main()