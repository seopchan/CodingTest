# 2304 / 창고 다각형

"""
지붕 
1. 수평, 수직 모두 연결
2. 수평은 기둥 윗면, 수직은 기둥 옆면
3. 가장자리는 땅
4. 오목하면 안 됨

즉, 최고점 기준으로 왼쪽, 오른쪽으로 내려가기만 함 'ㅅ'형태
"""

"""
스택 사용
최고기둥에서 다음 왼쪽 최고 기둥까지 계산
오목한 부분이 있으면 안되기 때문에
두 기둥 사이의 면적은
(최고 index - 2번 index) * 2번 height

맨 첫 기둥까지 반복

최고 기둥에서 다음 오른쪽 최고 기둥까지 계산
왼쪽과 동일하게 반복
"""

import sys
input = sys.stdin.readline

def calcSideArea(pillars, maxBasePos, isLR):
    stack = [] # [{높이: num, 넓이: num, pos: num}]

    for pos, height in pillars:
        # 이전 높이보다 높거나 같으면
        # 기존 넓이 무시 후 새로 넓이 계산
        while stack and height >= stack[-1]['height']:
            stack.pop()

        # 더 높은 이전 기둥 기준 넓이 계산해서 추가
        basePos = stack[-1]['pos'] if stack else maxBasePos

        # 넓이 계산 후 스택에 추가
        width = (basePos - pos) if isLR == 'L' else (pos - basePos)
        newArea = height * width
        stack.append({'height': height, 'area': newArea, 'pos': pos})

    sum = 0
    for p in stack:
        sum += p['area']
    return sum

def calcArea(pillars):
    # 기둥을 위치 기준으로 정렬
    pillars.sort()

    # 가장 높은 기둥 찾기
    maxIndex, maxP = max(enumerate(pillars), key=lambda idxPillar: idxPillar[1][1])
    maxPillarPos, maxHeight = maxP
    
    area = 0
    area += calcSideArea(pillars[maxIndex - 1::-1], maxPillarPos, 'L')
    area += calcSideArea(pillars[maxIndex + 1::], maxPillarPos, 'R')
    
    # 최고 기둥이 포함된 면적 추가
    area += maxHeight
    print(area)

n = int(input())
pillars = [tuple(map(int, input().strip().split())) for _ in range(n)]
calcArea(pillars)
