# 1182 / 부분수열의 합

"""
조합으로 모든 가능한 부분수열 구하기
"""
from itertools import combinations

def main(n, nums, target):
    answer = 0
    # 모든 가능한 부분수열(조합)을 1부터 n까지 생성
    for i in range(1, n + 1):
        for combi in combinations(nums, i):
            if sum(combi) == target:
                answer += 1
    print(answer)

N, S = map(int, input().split())
nums = list(map(int, input().strip().split()))
main(N, nums, S)