# 3649 / 로봇 프로젝트

"""
x cm / a + b = x

레고 100만개 -> 이분탐색
"""
import sys
input = sys.stdin.readline

def readInput():
    holeWidthCm = int(input().strip())
    n = int(input().strip())
    legoLengthsNm = [int(input().strip()) for _ in range(n)]
    return holeWidthCm, legoLengthsNm

def binarySearch(legoLengthsNm, target):
    legoLengthsNm.sort()
    left, right = 0, len(legoLengthsNm) - 1
    bestPair = None

    while left < right:
        currentSum = legoLengthsNm[left] + legoLengthsNm[right]
        if currentSum == target:
            if not bestPair or abs(legoLengthsNm[left] - legoLengthsNm[right]) > abs(bestPair[0] - bestPair[1]):
                bestPair = (legoLengthsNm[left], legoLengthsNm[right])
            left += 1
            right -= 1
        elif currentSum < target:
            left += 1
        else:
            right -= 1

    return bestPair

def main():
    while True:
        try:
            holeWidthCm, legoLengthsNm = readInput()
            holeWidthNm = holeWidthCm * 10000000  # 구멍의 너비를 나노미터로 변환

            if not legoLengthsNm:
                print("danger")
                continue

            answer = binarySearch(legoLengthsNm, holeWidthNm)
            if answer:
                print(f'yes {answer[0]} {answer[1]}')
            else:
                print("danger")
        except:
            break

main()