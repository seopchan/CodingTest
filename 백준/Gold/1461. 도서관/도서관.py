# 1461 / 도서관

"""
세준 0 책 0
책들을 원래 위치로, 정수 |10,000|
한번에 M개

1. 책 위치 분리 및 정렬
    책 위치 음수, 양수 분리 -> 절댓값 기준 정렬
    가장 먼 책부터 처리
2. 책 위치 M개 그룹화
    최소한의 이동거리
3. 각 그룹의 제일 먼 위치까지 왕복 계산
    단, 맨 마지막은 편도

당장 가능한 최선의 선택으로 최적해 구하기 -> 그리디
"""

def calcSteps(posArr, m):
    steps = 0
    while posArr:
        # 제일 먼 위치 왕복 계산
        steps += abs(posArr.pop()) * 2
        for _ in range(m - 1):
            if posArr:
                posArr.pop()
    return steps

def returnBooks(n, m, books):
    # 책 위치 음수, 양수 분리
    minusPosArr = []
    plusPosArr = []
    for pos in books:
        plusPosArr.append(pos) if pos > 0 else minusPosArr.append(pos)

    # 절댓값 기준 정렬
    minusPosArr.sort(key = abs)
    plusPosArr.sort()

    # 제일 먼 거리 구하기
    maxDist = 0
    if minusPosArr:
        maxDist = max(maxDist, abs(minusPosArr[-1]))
    if plusPosArr:
        maxDist = max(maxDist, plusPosArr[-1])

    # 각 그룹의 제일 먼 위치까지 왕복 계산
    steps = calcSteps(minusPosArr, m) + calcSteps(plusPosArr, m)

    # 제일 먼 거리 한번 빼기 (마지막은 편도)
    return (steps - maxDist)

def main():
    n, m = map(int, input().split())
    books = list(map(int, input().strip().split()))

    print(returnBooks(n, m, books))

main()